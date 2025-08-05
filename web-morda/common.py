"""
Common utility functions shared across the application
"""

import os
import json
from typing import Dict

# Global debug configuration
_debug_config = None


def load_debug_config(data_dir: str = 'data') -> Dict:
    """Load debug configuration from JSON file"""
    global _debug_config
    
    if _debug_config is not None:
        return _debug_config
    
    debug_file = os.path.join(data_dir, 'debug_config.json')
    
    if not os.path.exists(debug_file):
        # Create default debug config file
        default_config = {
            "debug_enabled": False,
            "description": "Debug configuration for RAC utilities and web application",
            "settings": {
                "print_rac_commands": True,
                "print_rac_output": True,
                "print_session_operations": True,
                "print_cluster_operations": True,
                "print_authentication": False,
                "flask_debug": False
            }
        }
        os.makedirs(data_dir, exist_ok=True)
        with open(debug_file, 'w') as f:
            json.dump(default_config, f, indent=2)
        _debug_config = default_config
        return _debug_config
    
    try:
        with open(debug_file, 'r') as f:
            _debug_config = json.load(f)
            return _debug_config
    except Exception as e:
        print(f"[RAC WARNING] Failed to load debug config: {e}")
        _debug_config = {"debug_enabled": False, "settings": {}}
        return _debug_config