"""
RAC (Remote Administration Console) utility functions
Based on the library provided by your friend, adapted for our web panel
"""

import subprocess
import os
from typing import List, Dict, Optional, Tuple


def run_command(description: str, command: str, timeout: int = 30) -> Tuple[List[str], str, str]:
    """Execute a command and return (output_lines, stdout, stderr)"""
    try:
        # Log the command for debugging
        print(f"[RAC DEBUG] {description}: {command}")
        
        # Get RAC path from environment or find it
        rac_executable = os.environ.get('RAC_PATH')
        
        if not rac_executable:
            # Set RAC path - check common locations
            rac_paths = [
                '/opt/1cv8/x86_64/current/rac',  # Linux
                '/Applications/1cv8/current/rac',  # macOS
                'rac',  # System PATH
                'rac.exe',  # Windows in PATH
            ]
            
            # Find working RAC executable
            for path in rac_paths:
                try:
                    test_result = subprocess.run([path, '--help'], capture_output=True, timeout=5)
                    if test_result.returncode == 0 or b'Usage:' in test_result.stdout:
                        rac_executable = path
                        print(f"[RAC DEBUG] Found RAC at: {path}")
                        break
                except:
                    continue
            
            if not rac_executable:
                rac_executable = 'rac'  # Fallback
                print(f"[RAC DEBUG] Using fallback RAC command: {rac_executable}")
        else:
            print(f"[RAC DEBUG] Using RAC_PATH from environment: {rac_executable}")
        
        # Replace 'rac' in command with full path
        if command.startswith('rac '):
            command = command.replace('rac ', f'"{rac_executable}" ', 1)
        elif command.startswith('rac.exe '):
            command = command.replace('rac.exe ', f'"{rac_executable}" ', 1)
        
        print(f"[RAC DEBUG] Executing: {command}")
        
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=timeout
        )
        
        print(f"[RAC DEBUG] Return code: {result.returncode}")
        if result.stdout:
            print(f"[RAC DEBUG] stdout: {result.stdout}")
        if result.stderr:
            print(f"[RAC DEBUG] stderr: {result.stderr}")
        
        if result.returncode != 0:
            error_msg = f"Command failed (code {result.returncode})"
            if result.stderr:
                error_msg += f": {result.stderr}"
            if result.stdout:
                error_msg += f" | stdout: {result.stdout}"
            raise Exception(error_msg)
            
        output_lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
        return output_lines, result.stdout, result.stderr
    
    except subprocess.TimeoutExpired:
        error_msg = f"Command timed out after {timeout} seconds"
        print(f"[RAC ERROR] {error_msg}")
        raise Exception(error_msg)
    except Exception as e:
        print(f"[RAC ERROR] {str(e)}")
        raise Exception(f"Command execution failed: {str(e)}")


def process_output(output: List[str], separator: str = '') -> List[Dict[str, str]]:
    """Process RAC output into structured data"""
    objects = []
    is_new_object = True
    
    for line in output:
        if not line and line != separator:
            continue
            
        if (line.startswith(separator) and bool(separator)) or separator == line:
            is_new_object = True
            continue
            
        if is_new_object:
            obj = {}
            objects.append(obj)
            is_new_object = False
            
        if ':' in line:
            key, value = line.replace(' ', '').split(':', maxsplit=1)
            obj[key] = value
            
    return objects


def add_cluster_credentials(command: str, cluster_user: str = '', cluster_pwd: str = '') -> str:
    """Add cluster credentials to RAC command"""
    if cluster_user:
        command += f' --cluster-user={cluster_user}'
    if cluster_pwd:
        command += f' --cluster-pwd={cluster_pwd}'
    return command


def add_infobase_credentials(command: str, username: str = '', pwd: str = '') -> str:
    """Add infobase credentials to RAC command"""
    if username and pwd:
        command += f' --infobase-user={username} --infobase-pwd={pwd}'
    elif username:
        command += f' --infobase-user={username}'
    return command


def get_rac_address(server: str, cluster_port: str) -> str:
    """Convert cluster address to RAC address"""
    # Handle the port mapping logic
    if cluster_port == "1541":
        return f"{server}:1545"
    elif cluster_port == "2541":
        return f"{server}:2545"
    elif cluster_port.endswith("2541"):
        return f"{server}:2545"
    else:
        # Default mapping or use provided port + 4
        try:
            port_num = int(cluster_port)
            rac_port = port_num + 4
            return f"{server}:{rac_port}"
        except ValueError:
            return f"{server}:1545"  # Default fallback


class RACManager:
    """RAC Manager class for handling 1C cluster operations"""
    
    def __init__(self, server: str, cluster_port: str, cluster_user: str = '', cluster_pwd: str = ''):
        self.server = server
        self.cluster_port = cluster_port
        self.rac_address = get_rac_address(server, cluster_port)
        self.cluster_user = cluster_user
        self.cluster_pwd = cluster_pwd
        self._cluster_id = None
    
    def get_cluster_id(self) -> str:
        """Get cluster ID for the server"""
        if self._cluster_id:
            return self._cluster_id
            
        command = f'rac cluster list {self.rac_address}'
        
        try:
            output, stdout, stderr = run_command('Getting cluster ID', command)
            clusters = process_output(output, '')
            
            if not clusters:
                raise Exception("No clusters found")
                
            self._cluster_id = clusters[0].get('cluster', '')
            if not self._cluster_id:
                raise Exception("Cluster ID not found in response")
                
            return self._cluster_id
            
        except Exception as e:
            raise Exception(f"Failed to get cluster ID: {str(e)}")
    
    def get_clusters_list(self) -> List[Dict[str, str]]:
        """Get list of all clusters"""
        command = f'rac cluster list {self.rac_address}'
        
        try:
            output, stdout, stderr = run_command('Getting clusters list', command)
            return process_output(output, '')
        except Exception as e:
            raise Exception(f"Failed to get clusters list: {str(e)}")
    
    def get_infobases_list(self, cluster_id: str = None) -> List[Dict[str, str]]:
        """Get list of infobases for a cluster"""
        if not cluster_id:
            cluster_id = self.get_cluster_id()
            
        command = f'rac infobase summary list --cluster={cluster_id}'
        command = add_cluster_credentials(command, self.cluster_user, self.cluster_pwd)
        command += f' {self.rac_address}'
        
        try:
            output, stdout, stderr = run_command('Getting infobases list', command)
            return process_output(output, '')
        except Exception as e:
            raise Exception(f"Failed to get infobases list: {str(e)}")
    
    def get_infobase_id(self, ib_name: str, cluster_id: str = None) -> str:
        """Get infobase ID by name"""
        infobases = self.get_infobases_list(cluster_id)
        
        for ib in infobases:
            if ib.get('name', '').lower() == ib_name.lower():
                return ib.get('infobase', '')
                
        raise Exception(f"Infobase '{ib_name}' not found")
    
    def get_sessions_list(self, infobase_id: str, cluster_id: str = None, ib_user: str = '', ib_pwd: str = '') -> List[Dict[str, str]]:
        """Get sessions list for an infobase"""
        if not cluster_id:
            cluster_id = self.get_cluster_id()
            
        command = f'rac session list --cluster={cluster_id} --infobase={infobase_id}'
        # command = add_infobase_credentials(command, ib_user, ib_pwd)
        command = add_cluster_credentials(command, self.cluster_user, self.cluster_pwd)
        command += f' {self.rac_address}'
        
        try:
            output, stdout, stderr = run_command('Getting sessions list', command)
            return process_output(output, 'data-separation')
        except Exception as e:
            raise Exception(f"Failed to get sessions list: {str(e)}")
    
    def terminate_session(self, session_id: str, cluster_id: str = None, ib_user: str = '', ib_pwd: str = '') -> Tuple[bool, str, str]:
        """Terminate a specific session. Returns (success, stdout, stderr)"""
        if not cluster_id:
            cluster_id = self.get_cluster_id()
            
        command = f'rac session terminate --cluster={cluster_id} --session={session_id}'
        # command = add_infobase_credentials(command, ib_user, ib_pwd)
        command = add_cluster_credentials(command, self.cluster_user, self.cluster_pwd)
        command += f' {self.rac_address}'
        
        try:
            output, stdout, stderr = run_command('Terminating session', command)
            return True, stdout, stderr
        except Exception as e:
            raise Exception(f"Failed to terminate session: {str(e)}")
    
    def terminate_all_sessions(self, infobase_id: str, cluster_id: str = None, ib_user: str = '', ib_pwd: str = '') -> Tuple[int, int, List[str]]:
        """Terminate all sessions for an infobase. Returns (terminated_count, failed_count, error_messages)"""
        sessions = self.get_sessions_list(infobase_id, cluster_id, ib_user, ib_pwd)
        
        terminated_count = 0
        failed_count = 0
        error_messages = []
        
        for session in sessions:
            session_id = session.get('session')
            if session_id:
                try:
                    success, stdout, stderr = self.terminate_session(session_id, cluster_id, ib_user, ib_pwd)
                    if success:
                        terminated_count += 1
                    else:
                        failed_count += 1
                        error_messages.append(f"Session {session_id}: {stderr}")
                except Exception as e:
                    print(f"Failed to terminate session {session_id}: {e}")
                    failed_count += 1
                    error_messages.append(f"Session {session_id}: {str(e)}")
        
        return terminated_count, failed_count, error_messages
    
    # def set_sessions_deny(self, infobase_id: str, deny: bool, cluster_id: str = None, ib_user: str = '', ib_pwd: str = '') -> bool:
    #     """Enable/disable new sessions for an infobase"""
    #     if not cluster_id:
    #         cluster_id = self.get_cluster_id()
            
    #     mode = "on" if deny else "off"
    #     command = f'rac infobase update --cluster={cluster_id} --infobase={infobase_id} --sessions-deny={mode}'
    #     command = add_infobase_credentials(command, ib_user, ib_pwd)
    #     command = add_cluster_credentials(command, self.cluster_user, self.cluster_pwd)
    #     command += f' {self.rac_address}'
        
    #     try:
    #         run_command(f'Setting sessions deny to {mode}', command)
    #         return True
    #     except Exception as e:
    #         raise Exception(f"Failed to set sessions deny: {str(e)}")


def create_rac_manager_from_connection_string(conn_str: str, cluster_user: str = '', cluster_pwd: str = '') -> RACManager:
    """Create RAC manager from 1C connection string"""
    import re
    
    # Parse connection string: "Srvr=\"server:1541\";Ref=\"database_name\";" or "Srvr=server:1541;Ref=database_name;"
    # Handle both quoted and unquoted formats
    server_match = re.search(r'Srvr=(?:"([^"]+)"|([^;]+))', conn_str, re.IGNORECASE)
    
    if not server_match:
        raise Exception("Invalid connection string format")
    
    # Get the matched group (quoted or unquoted)
    server_port = server_match.group(1) or server_match.group(2)
    
    # Extract server and port
    if ':' in server_port:
        server, port = server_port.split(':', 1)
    else:
        server = server_port
        port = "1541"  # Default port
    
    return RACManager(server, port, cluster_user, cluster_pwd)
