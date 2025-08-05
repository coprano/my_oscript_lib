from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import subprocess
import json
import re
import os
from datetime import datetime
import hashlib
from functools import wraps
import secrets
import string
from rac_utils import RACManager, create_rac_manager_from_connection_string

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this in production

# Configuration
DATA_DIR = os.environ.get('DATA_DIR', 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
LOGS_FILE = os.path.join(DATA_DIR, 'logs.json')
MESSAGE_FILE = os.path.join(DATA_DIR, 'system_message.json')

# Cluster credentials from environment
DEFAULT_CLUSTER_USER = os.environ.get('CLUSTER_USER', '')
DEFAULT_CLUSTER_PWD = os.environ.get('CLUSTER_PWD', '')

# RAC port mappings (kept for backward compatibility)
RAC_PORT_MAP = {
    '1541': '1545',
    '2541': '2545'
}

def load_users():
    """Load users from JSON file"""
    if not os.path.exists(USERS_FILE):
        # Create default users file with enhanced structure
        default_users = {
            'petrovma': {
                'password_hash': hashlib.sha256('password123'.encode()).hexdigest(),
                'whitelisted_bases': [],
                'is_admin': False
            },
            'admin': {
                'password_hash': hashlib.sha256('admin123'.encode()).hexdigest(),
                'whitelisted_bases': [],
                'is_admin': True
            }
        }
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_users, f, indent=2, ensure_ascii=False)
        return default_users
    
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        users = json.load(f)
        
    # Migrate old format to new format if needed
    migrated = False
    for username, user_data in users.items():
        if isinstance(user_data, str):  # Old format: username -> password_hash
            users[username] = {
                'password_hash': user_data,
                'whitelisted_bases': [],
                'is_admin': username == 'admin'
            }
            migrated = True
    
    if migrated:
        save_users(users)
    
    return users

def save_users(users):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

def generate_password(length=12):
    """Generate a secure random password"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for _ in range(length))

def filter_databases_for_user(databases, username, user_data):
    """Filter databases based on user permissions"""
    # Admin users have access to all databases
    if user_data.get('is_admin', False):
        return databases
    
    # Regular users: databases containing username OR matching whitelisted patterns
    filtered = []
    whitelisted_bases = user_data.get('whitelisted_bases', [])
    
    for db in databases:
        db_name = db.get('name', '').lower()
        
        # Check if database contains username
        if username.lower() in db_name:
            filtered.append(db)
            continue
        
        # Check whitelisted patterns
        for pattern in whitelisted_bases:
            if pattern.strip():  # Skip empty patterns
                pattern = pattern.strip().lower()
                # Simple wildcard matching
                if pattern.startswith('*') and pattern.endswith('*'):
                    # *pattern* - contains
                    if pattern[1:-1] in db_name:
                        filtered.append(db)
                        break
                elif pattern.startswith('*'):
                    # *pattern - ends with
                    if db_name.endswith(pattern[1:]):
                        filtered.append(db)
                        break
                elif pattern.endswith('*'):
                    # pattern* - starts with
                    if db_name.startswith(pattern[:-1]):
                        filtered.append(db)
                        break
                else:
                    # exact match
                    if db_name == pattern:
                        filtered.append(db)
                        break
    
    return filtered

def log_action(username, action, details=""):
    """Log user actions"""
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'username': username,
        'action': action,
        'details': details
    }
    
    logs = []
    if os.path.exists(LOGS_FILE):
        with open(LOGS_FILE, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    
    logs.append(log_entry)
    
    # Keep only last 1000 log entries
    if len(logs) > 1000:
        logs = logs[-1000:]
    
    with open(LOGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

def load_system_message():
    """Load system message from JSON file"""
    if not os.path.exists(MESSAGE_FILE):
        return {"enabled": False, "message": ""}
    
    try:
        with open(MESSAGE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"enabled": False, "message": ""}

def save_system_message(message_data):
    """Save system message to JSON file"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(MESSAGE_FILE, 'w', encoding='utf-8') as f:
        json.dump(message_data, f, indent=2, ensure_ascii=False)

def login_required(f):
    """Decorator to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator to require admin privileges"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        
        users = load_users()
        user_data = users.get(session['username'], {})
        if not user_data.get('is_admin', False):
            flash('Admin privileges required')
            return redirect(url_for('index'))
        
        return f(*args, **kwargs)
    return decorated_function

# def parse_connection_string(conn_str):
#     """Parse 1C connection string and extract server info"""
#     # Example: "Srvr=\"server:1541\";Ref=\"database_name\";" or "Srvr=server:1541;Ref=database_name;"
#     # Handle both quoted and unquoted formats
#     server_match = re.search(r'Srvr=(?:"([^"]+)"|([^;]+))', conn_str, re.IGNORECASE)
#     ref_match = re.search(r'Ref=(?:"([^"]+)"|([^;]+))', conn_str, re.IGNORECASE)
    
#     if not server_match:
#         return None, None, None
    
#     # Get the matched group (quoted or unquoted)
#     server_port = server_match.group(1) or server_match.group(2)
#     database = (ref_match.group(1) or ref_match.group(2)) if ref_match else ""
    
#     # Extract server and port
#     if ':' in server_port:
#         server, port = server_port.split(':')
#         rac_port = RAC_PORT_MAP.get(port, str(int(port) + 4) if port.isdigit() else "1545")
#         return server, port, rac_port
#     else:
#         return server_port, "1541", "1545"

@app.route('/')
@login_required
def index():
    print(f"Index route accessed by user: {session['username']}")
    return render_template('index.html', 
                         username=session['username'], 
                         is_admin=session.get('is_admin', False))

@app.route('/admin')
@admin_required
def admin():
    users = load_users()
    return render_template('admin.html', 
                         username=session['username'],
                         users=users)

@app.route('/test')
def test():
    return '<h1>Test page working!</h1>'

@app.route('/health')
def health():
    return jsonify({
        'status': 'ok',
        'users_file_exists': os.path.exists(USERS_FILE),
        'logs_file_exists': os.path.exists(LOGS_FILE),
        'templates_dir': os.path.exists('templates'),
        'login_template': os.path.exists('templates/login.html'),
        'index_template': os.path.exists('templates/index.html')
    })

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(f"Login route accessed, method: {request.method}")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = load_users()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        user_data = users.get(username, {})
        if user_data and user_data.get('password_hash') == password_hash:
            session['username'] = username
            session['is_admin'] = user_data.get('is_admin', False)
            log_action(username, 'login')
            print(f"User {username} logged in successfully")
            return redirect(url_for('index'))
        else:
            print(f"Failed login attempt for user: {username}")
            flash('Invalid username or password')
    
    print("Rendering login template")
    return render_template('login.html')

@app.route('/logout')
def logout():
    username = session.get('username', 'unknown')
    log_action(username, 'logout')
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/api/get_clusters', methods=['POST'])
@login_required
def get_clusters():
    """Get cluster list from connection string"""
    data = request.json
    conn_str = data.get('connection_string', '')
    
    try:
        # Use environment cluster credentials by default
        cluster_user = DEFAULT_CLUSTER_USER
        cluster_pwd = DEFAULT_CLUSTER_PWD
        
        # Create RAC manager from connection string
        rac_manager = create_rac_manager_from_connection_string(
            conn_str, cluster_user, cluster_pwd, DATA_DIR
        )
        
        # Get clusters list
        clusters = rac_manager.get_clusters_list()
        
        log_action(session['username'], 'get_clusters', f"Server: {rac_manager.server}:{rac_manager.cluster_port}")
        
        return jsonify({
            'success': True, 
            'clusters': clusters,
            'server': rac_manager.server,
            'cluster_port': rac_manager.cluster_port,
            'rac_port': rac_manager.rac_address.split(':')[1]
        })
        
    except Exception as e:
        log_action(session['username'], 'get_clusters_error', str(e))
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/get_databases', methods=['POST'])
@login_required
def get_databases():
    """Get databases for a cluster"""
    data = request.json
    cluster_id = data.get('cluster_id')
    server = data.get('server')
    cluster_port = data.get('cluster_port')
    
    print(f"[DEBUG] get_databases called with data: {data}")
    print(f"[DEBUG] cluster_id: {cluster_id}")
    print(f"[DEBUG] server: {server}")
    print(f"[DEBUG] cluster_port: {cluster_port}")
    
    try:
        # Use environment cluster credentials
        cluster_user = DEFAULT_CLUSTER_USER
        cluster_pwd = DEFAULT_CLUSTER_PWD
        
        # Create RAC manager
        rac_manager = RACManager(server, cluster_port, cluster_user, cluster_pwd, DATA_DIR)
        
        # Get databases list
        databases = rac_manager.get_infobases_list(cluster_id)
        
        # Filter databases by user permissions
        username_filter = session['username']
        users = load_users()
        user_data = users.get(username_filter, {})
        
        filtered_databases = filter_databases_for_user(databases, username_filter, user_data)
        
        log_action(session['username'], 'get_databases', 
                  f"Cluster: {cluster_id}, Total: {len(databases)}, Accessible: {len(filtered_databases)}, Is Admin: {user_data.get('is_admin', False)}")
        
        return jsonify({
            'success': True, 
            'databases': filtered_databases
        })
        
    except Exception as e:
        log_action(session['username'], 'get_databases_error', str(e))
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/get_sessions', methods=['POST'])
@login_required
def get_sessions():
    """Get sessions for a database"""
    data = request.json
    cluster_id = data.get('cluster_id')
    infobase_id = data.get('infobase_id')
    server = data.get('server')
    cluster_port = data.get('cluster_port')
    
    print(f"[DEBUG] get_sessions called with data: {data}")
    print(f"[DEBUG] cluster_id: {cluster_id}")
    print(f"[DEBUG] infobase_id: {infobase_id}")
    print(f"[DEBUG] server: {server}")
    print(f"[DEBUG] cluster_port: {cluster_port}")
    
    try:
        # Use environment cluster credentials
        cluster_user = DEFAULT_CLUSTER_USER
        cluster_pwd = DEFAULT_CLUSTER_PWD
        
        # Create RAC manager
        rac_manager = RACManager(server, cluster_port, cluster_user, cluster_pwd, DATA_DIR)
        
        # Get sessions list
        sessions = rac_manager.get_sessions_list(infobase_id, cluster_id)
        
        print(f"[DEBUG] Raw sessions returned: {sessions}")
        print(f"[DEBUG] Number of sessions: {len(sessions)}")
        for i, session_data in enumerate(sessions):
            print(f"[DEBUG] Session {i}: {session_data}")
        
        log_action(session['username'], 'get_sessions', f"Database: {infobase_id}, Sessions: {len(sessions)}")
        
        return jsonify({
            'success': True, 
            'sessions': sessions
        })
        
    except Exception as e:
        log_action(session['username'], 'get_sessions_error', str(e))
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/terminate_session', methods=['POST'])
@login_required
def terminate_session():
    """Terminate a session"""
    data = request.json
    cluster_id = data.get('cluster_id')
    session_id = data.get('session_id')
    server = data.get('server')
    cluster_port = data.get('cluster_port')
    
    try:
        # Use environment cluster credentials
        cluster_user = DEFAULT_CLUSTER_USER
        cluster_pwd = DEFAULT_CLUSTER_PWD
        
        # Create RAC manager
        rac_manager = RACManager(server, cluster_port, cluster_user, cluster_pwd, DATA_DIR)
        
        # Terminate session
        success, stdout, stderr = rac_manager.terminate_session(session_id, cluster_id)
        
        log_action(session['username'], 'terminate_session', f"Session: {session_id}")
        
        return jsonify({
            'success': True,
            'stdout': stdout,
            'stderr': stderr
        })
        
    except Exception as e:
        log_action(session['username'], 'terminate_session_error', f"Session: {session_id}, Error: {str(e)}")
        return jsonify({
            'success': False, 
            'error': str(e),
            'stdout': '',
            'stderr': ''
        })

@app.route('/api/terminate_all_sessions', methods=['POST'])
@login_required
def terminate_all_sessions():
    """Terminate all sessions for a database"""
    data = request.json
    cluster_id = data.get('cluster_id')
    infobase_id = data.get('infobase_id')
    server = data.get('server')
    cluster_port = data.get('cluster_port')
    
    try:
        # Use environment cluster credentials
        cluster_user = DEFAULT_CLUSTER_USER
        cluster_pwd = DEFAULT_CLUSTER_PWD
        
        # Create RAC manager
        rac_manager = RACManager(server, cluster_port, cluster_user, cluster_pwd, DATA_DIR)
        
        # Terminate all sessions
        terminated_count, failed_count, error_messages = rac_manager.terminate_all_sessions(infobase_id, cluster_id)
        
        log_action(session['username'], 'terminate_all_sessions', 
                  f"Database: {infobase_id}, Terminated: {terminated_count}, Failed: {failed_count}")
        
        return jsonify({
            'success': True,
            'terminated_count': terminated_count,
            'failed_count': failed_count,
            'error_messages': error_messages
        })
        
    except Exception as e:
        log_action(session['username'], 'terminate_all_sessions_error', f"Database: {infobase_id}, Error: {str(e)}")
        return jsonify({
            'success': False, 
            'error': str(e),
            'terminated_count': 0,
            'failed_count': 0,
            'error_messages': []
        })

# Admin API endpoints
@app.route('/api/admin/users', methods=['GET'])
@admin_required
def get_users():
    """Get all users for admin"""
    users = load_users()
    # Remove password hashes from response
    safe_users = {}
    for username, user_data in users.items():
        safe_users[username] = {
            'whitelisted_bases': user_data.get('whitelisted_bases', []),
            'is_admin': user_data.get('is_admin', False)
        }
    return jsonify({'success': True, 'users': safe_users})

@app.route('/api/admin/users', methods=['POST'])
@admin_required
def create_user():
    """Create a new user"""
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '')
    is_admin = data.get('is_admin', False)
    whitelisted_bases = data.get('whitelisted_bases', [])
    
    if not username or not password:
        return jsonify({'success': False, 'error': 'Username and password are required'})
    
    users = load_users()
    if username in users:
        return jsonify({'success': False, 'error': 'User already exists'})
    
    users[username] = {
        'password_hash': hashlib.sha256(password.encode()).hexdigest(),
        'whitelisted_bases': whitelisted_bases,
        'is_admin': is_admin
    }
    
    save_users(users)
    log_action(session['username'], 'create_user', f"Created user: {username}")
    
    return jsonify({'success': True})

@app.route('/api/admin/users/<username>', methods=['PUT'])
@admin_required
def update_user(username):
    """Update an existing user"""
    data = request.json
    users = load_users()
    
    if username not in users:
        return jsonify({'success': False, 'error': 'User not found'})
    
    # Update user data
    if 'password' in data and data['password']:
        users[username]['password_hash'] = hashlib.sha256(data['password'].encode()).hexdigest()
    
    if 'is_admin' in data:
        users[username]['is_admin'] = data['is_admin']
    
    if 'whitelisted_bases' in data:
        users[username]['whitelisted_bases'] = data['whitelisted_bases']
    
    save_users(users)
    log_action(session['username'], 'update_user', f"Updated user: {username}")
    
    return jsonify({'success': True})

@app.route('/api/admin/users/<username>', methods=['DELETE'])
@admin_required
def delete_user(username):
    """Delete a user"""
    if username == session['username']:
        return jsonify({'success': False, 'error': 'Cannot delete yourself'})
    
    users = load_users()
    if username not in users:
        return jsonify({'success': False, 'error': 'User not found'})
    
    del users[username]
    save_users(users)
    log_action(session['username'], 'delete_user', f"Deleted user: {username}")
    
    return jsonify({'success': True})

@app.route('/api/admin/users/bulk', methods=['POST'])
@admin_required
def bulk_create_users():
    """Create multiple users with auto-generated passwords"""
    data = request.json
    usernames = data.get('usernames', [])
    is_admin = data.get('is_admin', False)
    whitelisted_bases = data.get('whitelisted_bases', [])
    password_length = data.get('password_length', 12)
    
    if not usernames or not isinstance(usernames, list):
        return jsonify({'success': False, 'error': 'Usernames list is required'})
    
    # Validate password length
    if password_length < 8 or password_length > 32:
        password_length = 12
    
    users = load_users()
    results = []
    created_count = 0
    updated_count = 0
    
    for username in usernames:
        username = username.strip()
        if not username:
            continue
            
        # Generate a new password for each user
        generated_password = generate_password(password_length)
        password_hash = hashlib.sha256(generated_password.encode()).hexdigest()
        
        user_exists = username in users
        
        # Create or update user
        users[username] = {
            'password_hash': password_hash,
            'whitelisted_bases': whitelisted_bases,
            'is_admin': is_admin
        }
        
        if user_exists:
            updated_count += 1
            action = 'updated'
        else:
            created_count += 1
            action = 'created'
        
        results.append({
            'username': username,
            'password': generated_password,
            'action': action
        })
    
    if results:
        save_users(users)
        log_action(session['username'], 'bulk_create_users', 
                  f"Created: {created_count}, Updated: {updated_count}, Total users: {len(results)}")
    
    return jsonify({
        'success': True,
        'results': results,
        'summary': {
            'created': created_count,
            'updated': updated_count,
            'total': len(results)
        }
    })

@app.route('/api/get_servers', methods=['GET'])
@login_required
def get_servers():
    """Get whitelisted servers for dropdown"""
    try:
        from rac_utils import load_server_whitelist
        servers = load_server_whitelist(DATA_DIR)
        return jsonify({'success': True, 'servers': servers})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/message', methods=['GET'])
@admin_required
def get_system_message():
    """Get current system message"""
    try:
        message_data = load_system_message()
        return jsonify({'success': True, 'message': message_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/admin/message', methods=['POST'])
@admin_required
def set_system_message():
    """Set system message"""
    try:
        data = request.get_json()
        message_data = {
            "enabled": data.get('enabled', False),
            "message": data.get('message', '').strip()
        }
        
        save_system_message(message_data)
        log_action(session['username'], 'set_system_message', 
                  f"Enabled: {message_data['enabled']}, Message: {message_data['message'][:50]}...")
        
        return jsonify({'success': True, 'message': 'System message updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/message', methods=['GET'])
def get_public_system_message():
    """Get system message for display to all users"""
    try:
        message_data = load_system_message()
        if message_data.get('enabled', False) and message_data.get('message', '').strip():
            return jsonify({'success': True, 'message': message_data['message']})
        else:
            return jsonify({'success': True, 'message': ''})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Ensure data directory exists
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        print(f"Data directory: {DATA_DIR}")
    except Exception as e:
        print(f"Warning: Could not create data directory: {e}")
    
    print(f"Starting Flask app...")
    print(f"Users file: {USERS_FILE}")
    print(f"Logs file: {LOGS_FILE}")
    print(f"Cluster user configured: {'Yes' if DEFAULT_CLUSTER_USER else 'No'}")
    app.run(host='0.0.0.0', port=5005, debug=True)
