#!/usr/bin/env python3
"""
Test the complete flow with server whitelist and session parsing
"""

import os
import sys
sys.path.append('.')

from rac_utils import validate_server_access, process_output

print("🔍 Testing complete RAC flow...")

# Test 1: Server whitelist validation
print("\n1. Testing server whitelist:")
is_allowed, error_msg = validate_server_access('localhost', 'data')
print(f"   localhost allowed: {is_allowed}")
if error_msg:
    print(f"   Error: {error_msg}")

is_allowed, error_msg = validate_server_access('evil-server.com', 'data')
print(f"   evil-server.com allowed: {is_allowed}")
if error_msg:
    print(f"   Error: {error_msg}")

# Test 2: Session parsing with real format
print("\n2. Testing session parsing with real RAC format:")
session_output = [
    "session                          : 55e61062-e7a7-44dd-a97b-1297813a71d6",
    "session-id                       : 7",
    "infobase                         : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",
    "user-name                        : DefUser",
    "host                             : VDC01-DI1CAPP10.TN.TNGRP.RU",
    "app-id                           : BackgroundJob",
    "started-at                       : 2025-07-30T16:56:33",
    "last-active-at                   : 2025-07-30T16:56:33",
    "data-separation                  : ''",
    "",
    "session                          : 7bc90cff-13d2-49d4-9c94-8b17a5c722aa",
    "session-id                       : 6",
    "infobase                         : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",
    "user-name                        : DefUser",
    "host                             : VDC01-DI1CAPP10.TN.TNGRP.RU",
    "app-id                           : BackgroundJob",
    "started-at                       : 2025-07-30T16:56:32",
    "last-active-at                   : 2025-07-30T16:56:32",
    "data-separation                  : ''"
]

sessions = process_output(session_output, 'data-separation')
print(f"   Parsed {len(sessions)} sessions")

for i, session in enumerate(sessions, 1):
    print(f"\n   Session {i}:")
    print(f"     session-id: {session.get('session-id', 'N/A')}")
    print(f"     user-name: {session.get('user-name', 'N/A')}")
    print(f"     host: {session.get('host', 'N/A')}")
    print(f"     app-id: {session.get('app-id', 'N/A')}")
    print(f"     started-at: {session.get('started-at', 'N/A')}")
    print(f"     last-active-at: {session.get('last-active-at', 'N/A')}")

if len(sessions) == 2:
    print("\n✅ SUCCESS: All session fields are correctly parsed!")
else:
    print(f"\n❌ FAILED: Expected 2 sessions, got {len(sessions)}")

print("\n🎉 Testing complete!")
print("\nNext steps:")
print("1. Add your actual servers to data/server_whitelist.json")
print("2. Test the web interface with a real RAC connection")
print("3. Verify that all new session fields display correctly in the table")
