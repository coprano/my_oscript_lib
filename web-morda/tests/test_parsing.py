#!/usr/bin/env python3
"""
Test script to verify infobase and session parsing
"""

from rac_utils import process_output

# Test infobase summary parsing
print("Testing infobase summary parsing...")
infobase_output = [
    "infobase  : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",
    "name       : test_db",
    "description : "
]

print("Input (infobase):")
for line in infobase_output:
    print(f"  '{line}'")

infobase_result = process_output(infobase_output, '')
print("\nOutput (infobase):")
print(infobase_result)

if infobase_result and len(infobase_result) > 0:
    infobase_id = infobase_result[0].get('infobase', '')
    infobase_name = infobase_result[0].get('name', '')
    print(f"\nExtracted infobase ID: '{infobase_id}'")
    print(f"Extracted infobase name: '{infobase_name}'")
    if infobase_id and infobase_name:
        print("✓ SUCCESS: Infobase data successfully extracted!")
    else:
        print("✗ FAILED: Some infobase data is missing!")
else:
    print("✗ FAILED: No infobase objects parsed!")

print("\n" + "="*60)

# Test session parsing
print("\nTesting session parsing...")
session_output = [
    "session                          : 55e61062-e7a7-44dd-a97b-1297813a71d6",
    "session-id                       : 7",
    "infobase                         : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",
    "connection                       : 40e6a688-a29d-4768-99a6-11ee1630a54d",
    "process                          : 8d361844-c0bd-4678-b34a-d3470e3387b9",
    "user-name                        : DefUser",
    "host                             : VDC01-DI1CAPP10.TN.TNGRP.RU",
    "app-id                           : BackgroundJob",
    "locale                           : en_US",
    "started-at                       : 2025-07-30T16:56:33",
    "last-active-at                   : 2025-07-30T16:56:33",
    "hibernate                        : no",
    "data-separation                  : ''",
    "client-ip                        : ",
    "",  # Empty line separator
    "session                          : 7bc90cff-13d2-49d4-9c94-8b17a5c722aa",
    "session-id                       : 6",
    "infobase                         : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",
    "connection                       : bc99cfbd-8938-4383-8d1f-c4be7c94270e",
    "process                          : 8d361844-c0bd-4678-b34a-d3470e3387b9",
    "user-name                        : DefUser",
    "host                             : VDC01-DI1CAPP10.TN.TNGRP.RU",
    "app-id                           : BackgroundJob",
    "locale                           : en_US",
    "started-at                       : 2025-07-30T16:56:32",
    "last-active-at                   : 2025-07-30T16:56:32",
    "hibernate                        : no",
    "data-separation                  : ''",
    "client-ip                        : "
]

print("Input (sessions - truncated for readability):")
print("  First session fields...")

# Test with 'data-separation' as separator (as used in get_sessions_list)
session_result = process_output(session_output, 'data-separation')
print(f"\nOutput (sessions with data-separation separator):")
print(f"Number of sessions parsed: {len(session_result)}")

for i, session in enumerate(session_result):
    print(f"\nSession {i+1}:")
    print(f"  session: {session.get('session', 'N/A')}")
    print(f"  session-id: {session.get('session-id', 'N/A')}")
    print(f"  user-name: {session.get('user-name', 'N/A')}")
    print(f"  host: {session.get('host', 'N/A')}")
    print(f"  app-id: {session.get('app-id', 'N/A')}")
    print(f"  started-at: {session.get('started-at', 'N/A')}")
    print(f"  last-active-at: {session.get('last-active-at', 'N/A')}")

if len(session_result) == 2:
    print("\n✓ SUCCESS: Both sessions successfully parsed!")
else:
    print(f"\n✗ FAILED: Expected 2 sessions, got {len(session_result)}")

print("\n" + "="*60)
print("✓ Parsing tests completed!")
