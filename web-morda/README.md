# 1C RAC Session Manager

A web-based panel for managing 1C cluster sessions using RAC (Remote Administration Console).

## Features

- **User Authentication**: Enhanced file-based authentication system with admin roles
- **Admin Panel**: Full user management interface for administrators
- **Whitelisted Bases**: Allow users access to specific databases beyond name filtering
- **Connection String Parsing**: Input 1C connection strings to connect to servers
- **Environment-based Cluster Credentials**: Cluster credentials configured via Docker environment variables
- **Database Filtering**: Shows databases that contain the logged-in username OR match whitelisted patterns
- **Session Management**: Enhanced session management with individual selection, bulk operations, and "terminate all" functionality
- **Action Logging**: Comprehensive logging of all user actions and RAC commands
- **Debug Logging**: Enhanced RAC command logging for troubleshooting
- **Responsive UI**: Modern, mobile-friendly interface
- **Enhanced RAC Integration**: Uses optimized RAC utility based on proven library

## Quick Start with Docker

1. **Configure environment variables** in `docker-compose.yml`:
   ```yaml
   environment:
     - CLUSTER_USER=your_cluster_user
     - CLUSTER_PWD=your_cluster_password
   ```

2. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - Open http://localhost:5000 (or your server IP if accessing remotely)
   - Default users:
     - Username: `petrovma`, Password: `password123`
     - Username: `admin`, Password: `admin123`

## Manual Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

## Usage

1. **Configure cluster credentials** in your `docker-compose.yml` environment variables
2. **Login** with your username (default: `petrovma/password123` or `admin/admin123`)
3. **Admin users** can access the Admin Panel to:
   - Create, edit, and delete users
   - Set admin privileges
   - Configure whitelisted database patterns for users
4. **Enter Connection String** in format: `Srvr="server:1541";Ref="database_name";` (supports both quoted and unquoted formats)
5. **Select Cluster** from the list
6. **Select Database** (filtered to show databases containing your username OR matching your whitelisted patterns)
7. **Manage Sessions** - view sessions, select individual sessions or all sessions, and terminate them individually or in bulk

## Configuration

### Environment Variables
Set these in your `docker-compose.yml`:
- `CLUSTER_USER`: Username for cluster authentication
- `CLUSTER_PWD`: Password for cluster authentication
- `DATA_DIR`: Directory for storing user and log files (default: `/app/data`)

### RAC Port Mapping
The application automatically maps cluster ports to RAC ports:
- `1541` → `1545`
- `2541` → `2545`
- Other ports: `port + 4`

### User Management
- Users are stored in `users.json` with enhanced structure including admin privileges and whitelisted bases
- Default admin user: `admin/admin123` (can create and manage other users)
- Default regular user: `petrovma/password123`
- Admin users can access `/admin` panel for user management

### Database Access Control
- Users can access databases that contain their username in the name
- Additionally, admin can configure "whitelisted bases" patterns for each user
- Whitelisted patterns allow access to databases matching those patterns regardless of username

### Logging
All user actions and RAC commands are logged to `logs.json` with timestamps and detailed information.

## RAC Commands Used

The application uses these RAC commands:

1. **List Clusters:**
   ```bash
   rac cluster list <server:rac_port>
   ```

2. **List Databases:**
   ```bash
   rac infobase summary list --cluster <cluster_id> --cluster-user=<user> --cluster-pwd=<pwd> <server:rac_port>
   ```

3. **List Sessions:**
   ```bash
   rac session list --cluster <cluster_id> --infobase=<infobase_id> --cluster-user=<user> --cluster-pwd=<pwd> <server:rac_port>
   ```

4. **Terminate Session:**
   ```bash
   rac session terminate --cluster <cluster_id> --session=<session_id> --cluster-user=<user> --cluster-pwd=<pwd> <server:rac_port>
   ```

## Security Notes

- Change the Flask secret key in production
- Consider using HTTPS in production
- RAC credentials are handled securely (not logged)
- User passwords are hashed with SHA256

## File Structure

```
.
├── app.py                 # Main Flask application
├── rac_utils.py          # RAC utility functions (based on your friend's library)
├── templates/
│   ├── login.html        # Login page
│   └── index.html        # Main application page
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
├── users.json          # User credentials (auto-created)
└── logs.json           # Action logs (auto-created)
```

## Development

To run in development mode:

```bash
export FLASK_ENV=development
python app.py
```

The application will be available at http://localhost:5000 with debug mode enabled.
