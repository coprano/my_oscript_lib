#!/usr/bin/env python3
"""
Test infobase parsing with expected RAC output format
"""

from rac_utils import process_output

# Expected RAC infobase summary output format
infobase_output = [
    "infobase  : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",
    "name       : database1",
    "description : First database",
    "",  # separator
    "infobase  : 2750fdcf-60fe-5fe5-8912-fbb1da4b4c57", 
    "name       : database2",
    "description : Second database",
    "",
    "infobase  : 3860fdcf-70fe-6fe5-7912-fbb1da4b4c58",
    "name       : database3", 
    "description : Third database"
]

print("Testing infobase parsing...")
print("Expected multiple databases to be parsed:")

infobases = process_output(infobase_output, '')
print(f"\nParsed {len(infobases)} infobase(s)")

for i, ib in enumerate(infobases, 1):
    print(f"\nInfobase {i}:")
    for key, value in ib.items():
        print(f"  {key}: {value}")
    
    # Check what JavaScript expects
    print(f"  JavaScript expects:")
    print(f"    db.id: {ib.get('id', 'NOT FOUND')} vs db.infobase: {ib.get('infobase', 'NOT FOUND')}")
    print(f"    db.name: {ib.get('name', 'NOT FOUND')}")
    print(f"    db.descr: {ib.get('descr', 'NOT FOUND')} vs db.description: {ib.get('description', 'NOT FOUND')}")

if len(infobases) == 3:
    print(f"\n✅ SUCCESS: All {len(infobases)} infobases parsed correctly")
    print("JavaScript should use:")
    print("  db.infobase (not db.id)")
    print("  db.name") 
    print("  db.description (not db.descr)")
else:
    print(f"\n❌ ISSUE: Expected 3 infobases, got {len(infobases)}")
