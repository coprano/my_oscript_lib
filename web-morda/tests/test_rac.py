#!/usr/bin/env python3
"""
Test script to validate RAC installation and Docker setup
"""

import os
import subprocess
from rac_utils import run_command

def test_rac_executable():
    """Test if RAC executable can be found and executed"""
    print("=== Testing RAC Executable ===")
    
    # Check RAC_PATH environment variable
    rac_path = os.environ.get('RAC_PATH')
    if rac_path:
        print(f"RAC_PATH environment variable: {rac_path}")
        if os.path.exists(rac_path):
            print(f"✓ RAC executable exists at: {rac_path}")
        else:
            print(f"✗ RAC executable NOT found at: {rac_path}")
    else:
        print("RAC_PATH environment variable not set")
    
    # Test common RAC locations
    rac_paths = [
        '/opt/1cv8/x86_64/current/rac',  # Linux
        '/Applications/1cv8/current/rac',  # macOS
        'rac',  # System PATH
        'rac.exe',  # Windows in PATH
    ]
    
    print("\nTesting common RAC locations:")
    for path in rac_paths:
        try:
            result = subprocess.run([path, '--help'], capture_output=True, timeout=5)
            if result.returncode == 0 or b'Usage:' in result.stdout:
                print(f"✓ Working RAC found at: {path}")
                print(f"  Return code: {result.returncode}")
                if result.stdout:
                    first_line = result.stdout.decode('utf-8', errors='ignore').split('\n')[0]
                    print(f"  First line of output: {first_line}")
                break
            else:
                print(f"✗ RAC at {path} returned code {result.returncode}")
        except FileNotFoundError:
            print(f"✗ RAC not found at: {path}")
        except subprocess.TimeoutExpired:
            print(f"✗ RAC at {path} timed out")
        except Exception as e:
            print(f"✗ Error testing {path}: {e}")

def test_rac_utils():
    """Test our RAC utilities"""
    print("\n=== Testing RAC Utils ===")
    
    try:
        # Test run_command with a simple command
        output, stdout, stderr = run_command("Testing RAC help", "rac --help")
        print("✓ RAC utils working")
        print(f"  Output lines: {len(output)}")
        if stdout:
            print(f"  First line: {stdout.split(chr(10))[0] if chr(10) in stdout else stdout[:100]}")
    except Exception as e:
        print(f"✗ RAC utils failed: {e}")

def test_docker_volumes():
    """Test if we're running in Docker and volumes are mounted"""
    print("\n=== Testing Docker Volumes ===")
    
    # Check if we're in a container
    if os.path.exists('/.dockerenv'):
        print("✓ Running inside Docker container")
        
        # Check volume mounts
        if os.path.exists('/opt/1cv8'):
            print("✓ /opt/1cv8 volume mounted")
            # List contents
            try:
                contents = os.listdir('/opt/1cv8')
                print(f"  Contents: {contents[:5]}...")  # Show first 5 items
            except Exception as e:
                print(f"  Cannot list contents: {e}")
        else:
            print("✗ /opt/1cv8 volume NOT mounted")
            
        if os.path.exists('/app/data'):
            print("✓ /app/data volume mounted")
        else:
            print("✗ /app/data volume NOT mounted")
    else:
        print("Running outside Docker container")
        
        # Check local paths
        if os.path.exists('/opt/1cv8'):
            print("✓ /opt/1cv8 directory exists locally")
        else:
            print("✗ /opt/1cv8 directory not found locally")

def main():
    print("1C RAC Configuration Test")
    print("=" * 50)
    
    test_rac_executable()
    test_rac_utils()
    test_docker_volumes()
    
    print("\n" + "=" * 50)
    print("Test completed!")

if __name__ == "__main__":
    main()
