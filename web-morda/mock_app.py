#!/usr/bin/env python3
"""
Mock version of the RAC web application for testing UI features
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import json
import os
import hashlib
from functools import wraps
from datetime import datetime, timedelta
import random
import uuid
import logging

# Configure logging to console (like Docker logs)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # This outputs to console
    ]
)
logger = logging.getLogger('MockRAC')

app = Flask(__name__)
app.secret_key = 'mock-secret-key'

# Mock data
MOCK_SERVERS = [
    "server1.example.com:1541",
    "server2.example.com:1541", 
    "localhost:1541",
    "testserver:2541"
]

MOCK_CLUSTERS = [
    {"cluster": "cluster-uuid-1", "name": '"Production Cluster"'},
    {"cluster": "cluster-uuid-2", "name": "Test Cluster"},
    {"cluster": "cluster-uuid-3", "name": "Development Cluster"}
]

MOCK_DATABASES = [
    {"infobase": "db-uuid-1", "name": "MainDatabase", "description": "Main production database"},
    {"infobase": "db-uuid-2", "name": "TestDB", "description": "Testing database"},
    {"infobase": "db-uuid-3", "name": "AccountingDB", "description": "Accounting system database"},
    {"infobase": "db-uuid-4", "name": "HRMDB", "description": "Human resources management"},
    {"infobase": "db-uuid-5", "name": "InventoryDB", "description": "Inventory management system"},
    {"infobase": "db-uuid-6", "name": "SalesDB", "description": "Sales tracking database"}
]

def generate_mock_sessions(count=5):
    """Generate mock session data"""
    sessions = []
    users = ["admin", "petrovma", "user1", "user2", "analyst", "manager"]
    hosts = ["workstation-01", "laptop-05", "server-web", "client-pc-12"]
    
    for i in range(count):
        start_time = datetime.now() - timedelta(hours=random.randint(0, 24), minutes=random.randint(0, 59))
        last_active = start_time + timedelta(minutes=random.randint(1, 300))
        
        session_data = {
            "session": f"session-{uuid.uuid4().hex[:8]}",
            "session-id": str(random.randint(1, 1000)),
            "user-name": random.choice(users),
            "host": random.choice(hosts),
            "app-id": f"app-{random.randint(100, 999)}",
            "started-at": start_time.isoformat(),
            "last-active-at": last_active.isoformat()
        }
        sessions.append(session_data)
    
    return sessions

# Configuration
DATA_DIR = 'data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')

def load_users():
    """Load users from JSON file"""
    if not os.path.exists(USERS_FILE):
        os.makedirs(DATA_DIR, exist_ok=True)
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
        with open(USERS_FILE, 'w') as f:
            json.dump(default_users, f, indent=2)
        return default_users
    
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def login_required(f):
    """Decorator to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        logger.info(f"Login attempt for user: {username}")
        
        users = load_users()
        user_data = users.get(username)
        
        if user_data:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            if password_hash == user_data['password_hash']:
                session['username'] = username
                session['is_admin'] = user_data.get('is_admin', False)
                logger.info(f"Successful login for user: {username} (admin: {user_data.get('is_admin', False)})")
                flash('Login successful!')
                return redirect(url_for('index'))
        
        logger.warning(f"Failed login attempt for user: {username}")
        flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    username = session.get('username', 'unknown')
    logger.info(f"User logout: {username}")
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    logger.info(f"Index page accessed by user: {session['username']}")
    return render_template('index.html', 
                         username=session['username'], 
                         is_admin=session.get('is_admin', False))

@app.route('/api/get_servers')
@login_required
def get_servers():
    """Mock API endpoint for getting servers"""
    logger.info(f"get_servers requested by user: {session['username']}")
    return jsonify({
        'success': True,
        'servers': MOCK_SERVERS
    })

@app.route('/api/get_clusters', methods=['POST'])
@login_required
def get_clusters():
    """Mock API endpoint for getting clusters"""
    data = request.json
    conn_str = data.get('connection_string', '')
    
    logger.info(f"get_clusters requested by user: {session['username']}, connection: {conn_str}")
    
    # Simulate some processing time
    import time
    time.sleep(0.5)
    
    # Extract server from connection string
    server = "mock-server"
    if "Srvr=" in conn_str:
        try:
            server_part = conn_str.split('Srvr="')[1].split('"')[0]
            server = server_part.split(':')[0]
        except:
            pass
    
    logger.info(f"Returning {len(MOCK_CLUSTERS)} clusters to user: {session['username']}")
    
    return jsonify({
        'success': True,
        'clusters': MOCK_CLUSTERS,
        'server': server,
        'cluster_port': '1541',
        'rac_port': '1545'
    })

@app.route('/api/get_databases', methods=['POST'])
@login_required
def get_databases():
    """Mock API endpoint for getting databases"""
    data = request.json
    cluster_id = data.get('cluster_id')
    cluster_name = data.get('cluster_name', 'Unknown')
    
    logger.info(f"get_databases requested by user: {session['username']}, cluster: {cluster_name} ({cluster_id})")
    
    # Simulate some processing time
    import time
    time.sleep(0.3)
    
    # Filter databases based on username (for demo purposes)
    username = session['username']
    
    # Admin sees all databases, regular users see filtered list
    if session.get('is_admin', False):
        filtered_databases = MOCK_DATABASES
        logger.info(f"Admin user {username} - showing all {len(filtered_databases)} databases")
    else:
        # Regular users see databases that contain their username or common ones
        filtered_databases = [
            db for db in MOCK_DATABASES 
            if username.lower() in db['name'].lower() or 
               db['name'] in ['TestDB', 'MainDatabase']
        ]
        logger.info(f"Regular user {username} - showing {len(filtered_databases)} filtered databases")
    
    return jsonify({
        'success': True,
        'databases': filtered_databases
    })

@app.route('/api/get_sessions', methods=['POST'])
@login_required
def get_sessions():
    """Mock API endpoint for getting sessions"""
    data = request.json
    infobase_id = data.get('infobase_id')
    database_name = data.get('database_name', 'Unknown')
    
    logger.info(f"get_sessions requested by user: {session['username']}, database: {database_name} ({infobase_id})")
    
    # Simulate some processing time
    import time
    time.sleep(0.4)
    
    # Generate random number of sessions (0-8)
    session_count = random.randint(0, 8)
    sessions = generate_mock_sessions(session_count)
    
    logger.info(f"Returning {session_count} sessions for database {database_name} to user: {session['username']}")
    
    return jsonify({
        'success': True,
        'sessions': sessions
    })

@app.route('/api/terminate_session', methods=['POST'])
@login_required
def terminate_session():
    """Mock API endpoint for terminating a session"""
    data = request.json
    session_id = data.get('session_id')
    
    # Simulate some processing time
    import time
    time.sleep(0.2)
    
    # Simulate occasional failures for realism
    if random.randint(1, 10) == 1:  # 10% failure rate
        return jsonify({
            'success': False,
            'error': f'Failed to terminate session {session_id}: Session not found or already terminated'
        })
    
    return jsonify({
        'success': True,
        'stdout': f'Session {session_id} terminated successfully',
        'stderr': ''
    })

@app.route('/api/terminate_all_sessions', methods=['POST'])
@login_required
def terminate_all_sessions():
    """Mock API endpoint for terminating all sessions"""
    data = request.json
    
    # Simulate some processing time
    import time
    time.sleep(1.0)
    
    # Simulate terminating sessions
    total_sessions = random.randint(3, 10)
    terminated = random.randint(total_sessions - 2, total_sessions)
    failed = total_sessions - terminated
    
    error_messages = []
    if failed > 0:
        for i in range(failed):
            error_messages.append(f'Session session-{i+1}: Already terminated or not found')
    
    return jsonify({
        'success': True,
        'terminated_count': terminated,
        'failed_count': failed,
        'error_messages': error_messages
    })

if __name__ == '__main__':
    print("🚀 Starting Mock RAC Web Application...")
    print("📝 Login credentials:")
    print("   Username: admin, Password: admin123 (Admin user)")
    print("   Username: petrovma, Password: password123 (Regular user)")
    print("🌐 Open http://localhost:5050 in your browser")
    
    app.run(debug=True, host='0.0.0.0', port=5050)
