#!/usr/bin/env python3
"""
Test script to verify RAC cluster ID parsing fix
"""

from rac_utils import process_output

# Simulate RAC output format based on user's description
test_output = [
    "cluster           : 12345678-1234-1234-1234-123456789abc",
    "host               : test-server", 
    "port                : 1541",
    "name             : Main Cluster"
]

print("Testing process_output function with RAC cluster list format...")
print("Input:")
for line in test_output:
    print(f"  '{line}'")

result = process_output(test_output, '')
print("\nOutput:")
print(result)

if result and len(result) > 0:
    cluster_id = result[0].get('cluster', '')
    print(f"\nExtracted cluster ID: '{cluster_id}'")
    if cluster_id:
        print("✓ SUCCESS: Cluster ID successfully extracted!")
    else:
        print("✗ FAILED: Cluster ID is empty!")
else:
    print("✗ FAILED: No objects parsed from output!")
