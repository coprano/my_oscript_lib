#!/usr/bin/env python3
"""
Test that sessions are properly filtered by infobase
"""

from rac_utils import process_output

# Simulate session output that should be filtered by infobase
session_output = [
    "session                          : 55e61062-e7a7-44dd-a97b-1297813a71d6",
    "session-id                       : 7",
    "infobase                         : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",  # Target infobase
    "user-name                        : DefUser",
    "host                             : VDC01-DI1CAPP10.TN.TNGRP.RU",
    "app-id                           : BackgroundJob",
    "started-at                       : 2025-07-30T16:56:33",
    "last-active-at                   : 2025-07-30T16:56:33",
    "data-separation                  : ''",
    "",
    "session                          : 7bc90cff-13d2-49d4-9c94-8b17a5c722aa",
    "session-id                       : 6",
    "infobase                         : 2750fdcf-60fe-5fe5-8912-fbb1da4b4c57",  # Different infobase
    "user-name                        : AnotherUser",
    "host                             : VDC01-DI1CAPP10.TN.TNGRP.RU",
    "app-id                           : Designer",
    "started-at                       : 2025-07-30T16:56:32",
    "last-active-at                   : 2025-07-30T16:56:32",
    "data-separation                  : ''",
    "",
    "session                          : 8cd90cff-23d2-59d4-8c94-9b17a5c722bb",
    "session-id                       : 5", 
    "infobase                         : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",  # Target infobase again
    "user-name                        : ThirdUser",
    "host                             : VDC01-DI1CAPP10.TN.TNGRP.RU",
    "app-id                           : Enterprise",
    "started-at                       : 2025-07-30T16:55:15",
    "last-active-at                   : 2025-07-30T16:57:10",
    "data-separation                  : ''"
]

print("Testing session parsing and filtering...")
sessions = process_output(session_output, 'data-separation')
print(f"Parsed {len(sessions)} total sessions")

target_infobase = "1640fdcf-50fe-4fe5-9912-fbb1da4b4c56"
print(f"\nTarget infobase: {target_infobase}")

# This filtering should happen at RAC level with --infobase parameter
# But let's verify the parsing includes the infobase field
filtered_sessions = [s for s in sessions if s.get('infobase') == target_infobase]

print(f"\nSessions that would match target infobase: {len(filtered_sessions)}")
for i, session in enumerate(filtered_sessions, 1):
    print(f"\nSession {i}:")
    print(f"  session-id: {session.get('session-id', 'N/A')}")
    print(f"  user-name: {session.get('user-name', 'N/A')}")
    print(f"  infobase: {session.get('infobase', 'N/A')}")
    print(f"  app-id: {session.get('app-id', 'N/A')}")

print(f"\nAll sessions infobase fields:")
for i, session in enumerate(sessions, 1):
    print(f"  Session {i}: {session.get('infobase', 'N/A')} ({session.get('user-name', 'N/A')})")

if len(filtered_sessions) == 2:
    print(f"\n✅ SUCCESS: Correctly found 2 sessions for target infobase")
    print("Note: RAC should filter this automatically with --infobase parameter")
else:
    print(f"\n❌ Issue: Expected 2 sessions for target infobase, got {len(filtered_sessions)}")

print("\n" + "="*60)
print("RAC command should be:")
print(f"rac session list --cluster=CLUSTER_ID --infobase={target_infobase}")
print("This should return only the sessions for that specific infobase")
print("="*60)
