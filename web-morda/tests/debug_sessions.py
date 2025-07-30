#!/usr/bin/env python3
"""
Debug session parsing
"""

from rac_utils import process_output

# Simplified test with exact data structure
session_output = [
    "session                          : 55e61062-e7a7-44dd-a97b-1297813a71d6",
    "session-id                       : 7",
    "user-name                        : DefUser",
    "data-separation                  : ''",
    "",  # Empty line
    "session                          : 7bc90cff-13d2-49d4-9c94-8b17a5c722aa", 
    "session-id                       : 6",
    "user-name                        : AnotherUser",
    "data-separation                  : ''"
]

print("Debug: Session parsing with data-separation")
print("Input lines:")
for i, line in enumerate(session_output):
    print(f"  {i}: '{line}'")

result = process_output(session_output, 'data-separation')
print(f"\nResult: {len(result)} sessions")
for i, session in enumerate(result):
    print(f"Session {i+1}: {session}")
