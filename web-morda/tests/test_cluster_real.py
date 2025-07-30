#!/usr/bin/env python3
"""
Test cluster parsing with real RAC output
"""

from rac_utils import process_output

# Real RAC cluster output from the log
cluster_output = [
    "cluster                                   : 372981ac-b059-4739-92e0-83dcc80fe03e",
    "host                                      : server.test",
    "port                                      : 1541",
    "name                                      : \"Локальный кластер\"",
    "expiration-timeout                        : 0",
    "lifetime-limit                            : 0",
    "max-memory-size                           : 0",
    "max-memory-time-limit                     : 0",
    "security-level                            : 0",
    "session-fault-tolerance-level             : 0",
    "load-balancing-mode                       : performance",
    "errors-count-threshold                    : 0",
    "kill-problem-processes                    : 0",
    "kill-by-memory-with-dump                  : 0",
    "allow-access-right-audit-events-recording : 0",
    "ping-period                               : 0",
    "ping-timeout                              : 0",
    "restart-schedule                          : \"0 4 * * *\""
]

print("Testing cluster parsing with real RAC output...")
print("Input:")
for line in cluster_output[:5]:  # Show first 5 lines
    print(f"  '{line}'")
print("  ... (more fields)")

clusters = process_output(cluster_output, '')
print(f"\nParsed {len(clusters)} cluster(s)")

if clusters:
    cluster = clusters[0]
    print("\nCluster fields:")
    for key, value in cluster.items():
        print(f"  {key}: {value}")
    
    print(f"\nKey cluster ID field:")
    print(f"  cluster['cluster']: {cluster.get('cluster', 'NOT FOUND')}")
    print(f"  cluster['id']: {cluster.get('id', 'NOT FOUND')}")
    print(f"  cluster['name']: {cluster.get('name', 'NOT FOUND')}")
    
    expected_id = "372981ac-b059-4739-92e0-83dcc80fe03e"
    actual_id = cluster.get('cluster', '')
    
    if actual_id == expected_id:
        print(f"\n✅ SUCCESS: Cluster ID correctly parsed as '{actual_id}'")
        print("The frontend should use 'cluster.cluster' not 'cluster.id'")
    else:
        print(f"\n❌ FAILED: Expected '{expected_id}', got '{actual_id}'")
else:
    print("\n❌ FAILED: No clusters parsed")

print("\n" + "="*60)
print("JavaScript should use:")
print("  cluster.cluster (not cluster.id)")
print("  cluster.name")
print("="*60)
