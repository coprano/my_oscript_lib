#!/usr/bin/env python3
"""
Test script to verify server whitelist functionality
"""

from rac_utils import validate_server_access, load_server_whitelist

# Test loading whitelist
print("Testing server whitelist functionality...")

# Test 1: Load whitelist
print("\n1. Loading server whitelist:")
whitelist = load_server_whitelist('data')
print(f"   Whitelist: {whitelist}")

# Test 2: Validate allowed server
print("\n2. Testing allowed server (localhost):")
is_allowed, error_msg = validate_server_access('localhost', 'data')
print(f"   Allowed: {is_allowed}")
if error_msg:
    print(f"   Error: {error_msg}")

# Test 3: Validate blocked server
print("\n3. Testing blocked server (evil-server.com):")
is_allowed, error_msg = validate_server_access('evil-server.com', 'data')
print(f"   Allowed: {is_allowed}")
if error_msg:
    print(f"   Error: {error_msg}")

# Test 4: Case insensitive check
print("\n4. Testing case insensitive check (LOCALHOST):")
is_allowed, error_msg = validate_server_access('LOCALHOST', 'data')
print(f"   Allowed: {is_allowed}")
if error_msg:
    print(f"   Error: {error_msg}")

print("\n✓ Server whitelist tests completed!")
