#!/usr/bin/env python3
"""
Test infobase parsing with debugging
"""

from rac_utils import process_output

# Test data matching real RAC output format
test_infobase_data = [
    "infobase  : 1640fdcf-50fe-4fe5-9912-fbb1da4b4c56",
    "name       : database1", 
    "description : Test Database 1",
    "",  # Empty line separator
    "infobase  : 2750fdcf-60fe-5fe5-8912-fbb1da4b4c57",
    "name       : database2",
    "description : Test Database 2"
]

print("🔍 Testing infobase parsing...")
print("Input data:")
for i, line in enumerate(test_infobase_data):
    print(f"  {i}: '{line}'")

infobases = process_output(test_infobase_data, '')
print(f"\n📊 Parsed {len(infobases)} infobase(s)")

for i, ib in enumerate(infobases, 1):
    print(f"\n📋 Infobase {i}:")
    for key, value in ib.items():
        print(f"    {key}: {value}")
    
    # Check what the JavaScript will see
    db_id = ib.get('infobase') or ib.get('id')
    print(f"\n  🎯 JavaScript will get:")
    print(f"    db.infobase: {ib.get('infobase', 'UNDEFINED')}")
    print(f"    db.id: {ib.get('id', 'UNDEFINED')}")
    print(f"    db.name: {ib.get('name', 'UNDEFINED')}")
    print(f"    selectDatabase will be called with: '{db_id}', '{ib.get('name', 'UNDEFINED')}'")

if len(infobases) >= 1:
    first_ib = infobases[0]
    expected_id = "1640fdcf-50fe-4fe5-9912-fbb1da4b4c56"
    actual_id = first_ib.get('infobase', '')
    
    if actual_id == expected_id:
        print(f"\n✅ SUCCESS: Infobase ID correctly extracted as '{actual_id}'")
    else:
        print(f"\n❌ FAILED: Expected '{expected_id}', got '{actual_id}'")
else:
    print(f"\n❌ FAILED: No infobases parsed")

print("\n" + "="*60)
print("If infobase_id is still undefined, the issue is likely:")
print("1. Backend not sending correct field names")
print("2. Frontend database display not using correct fields") 
print("3. JavaScript template literal not evaluating correctly")
print("="*60)
