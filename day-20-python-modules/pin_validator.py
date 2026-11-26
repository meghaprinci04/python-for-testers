
import csv
from io import StringIO

csv_data = """TC_ID,PIN,Expected
TC01,8275,PASS
TC02,1234,PASS
TC03,ABCD,FAIL
TC04,123,FAIL
TC05,0123,PASS
"""

def validate_pin(pin):
    if pin.isdigit() and len(pin) == 4:
        return "PASS"
    else:
        return "FAIL"

file = StringIO(csv_data)
reader = csv.DictReader(file)

pass_count = 0
fail_count = 0

for row in reader:
    actual_result = validate_pin(row["PIN"])
    expected_result = row["Expected"]

    if actual_result == expected_result:
        print(row["TC_ID"], "- PASS")
        pass_count += 1
    else:
        print(row["TC_ID"], "- FAIL")
        fail_count += 1

print("\nExecution Summary")
print("Total Tests:", pass_count + fail_count)
print("Passed:", pass_count)
print("Failed:", fail_count)
