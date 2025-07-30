#!/usr/bin/env python3
"""
Final test of all bug fixes
"""

from rac_utils import process_output, load_server_whitelist

print("🔧 Testing all bug fixes...")

# Test 1: Multiple infobases parsing (Bug #1)
print("\n1. Testing multiple infobases parsing:")
infobase_output = [
    "infobase  : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",
    "name       : database1", 
    "description : First database",
    "",
    "infobase  : 2750fdcf-60fe-5fe5-8912-fbb1da4b4c57",
    "name       : database2",
    "description : Second database",
    "",
    "infobase  : 3860fdcf-70fe-6fe5-7912-fbb1da4b4c58",
    "name       : database3",
    "description : Third database"
]

infobases = process_output(infobase_output, '')
if len(infobases) == 3:
    print(f"   ✅ SUCCESS: Parsed {len(infobases)} infobases correctly")
    for i, ib in enumerate(infobases, 1):
        print(f"      DB{i}: {ib.get('name')} ({ib.get('infobase')[:8]}...)")
else:
    print(f"   ❌ FAILED: Expected 3 infobases, got {len(infobases)}")

# Test 2: Session parsing with data-separation (Bug #2 verification)
print("\n2. Testing session parsing:")
session_output = [
    "session: session1", "session-id: 1", "infobase: ib1", "user-name: user1", "data-separation: ''",
    "", 
    "session: session2", "session-id: 2", "infobase: ib2", "user-name: user2", "data-separation: ''"
]

sessions = process_output(session_output, 'data-separation')
if len(sessions) == 2:
    print(f"   ✅ SUCCESS: Parsed {len(sessions)} sessions correctly")
    for i, s in enumerate(sessions, 1):
        print(f"      Session{i}: {s.get('user-name')} (ID: {s.get('session-id')})")
else:
    print(f"   ❌ FAILED: Expected 2 sessions, got {len(sessions)}")

# Test 3: Server whitelist loading (Bug #3)
print("\n3. Testing server whitelist:")
try:
    servers = load_server_whitelist('data')
    if servers:
        print(f"   ✅ SUCCESS: Loaded {len(servers)} whitelisted servers")
        for server in servers:
            print(f"      - {server}")
    else:
        print("   ❌ FAILED: No servers in whitelist")
except Exception as e:
    print(f"   ❌ FAILED: Error loading whitelist: {e}")

print("\n🎉 All tests completed!")
print("\nChanges made:")
print("✅ Bug #1: Fixed infobase parsing to show all databases (not just last one)")
print("✅ Bug #2: Added debugging to track session filtering by infobase")  
print("✅ Bug #3: Replaced connection string input with server dropdown")
print("\nFrontend changes:")
print("- Updated JavaScript to use correct field names (cluster.cluster, db.infobase, db.description)")
print("- Added server dropdown with port selection")
print("- Added connection string preview")
print("\nBackend changes:")
print("- Fixed process_output() function to handle empty line separators")
print("- Added /api/get_servers endpoint")
print("- Added debugging to session endpoint")
