
import csv
from io import StringIO

# STEP 1: IVR test data
csv_data = """TC_ID,CUSTOMER,PIN,EXPECTED
TC01,Rahul,8275,PASS
TC02,Priya,ABCD,FAIL
TC03,Amit,123,PASS
TC04,Neha,,FAIL
TC05,Ravi,0123,PASS
TC06,Anita,5678,PASS
"""

# STEP 2: PIN validation function
def validate_pin(pin):
    try:
        if pin is None:
            raise TypeError("PIN is missing")

        if pin.isdigit() and len(pin) == 4:
            return "PASS"

        return "FAIL"

    except TypeError:
        return "FAIL"

# STEP 3: Read CSV data
file = StringIO(csv_data)
reader = csv.DictReader(file)

pass_count = 0
fail_count = 0

print("IVR PIN AUTOMATION REPORT")
print("=========================")

# STEP 4: Execute test cases
for row in reader:

    actual_result = validate_pin(row["PIN"])
    expected_result = row["EXPECTED"]

    if actual_result == expected_result:
        status = "PASS"
        pass_count += 1
    else:
        status = "FAIL"
        fail_count += 1

    print(
        row["TC_ID"],
        row["CUSTOMER"],
        "Expected:", expected_result,
        "Actual:", actual_result,
        "Test:", status
    )

# STEP 5: Execution summary
total_tests = pass_count + fail_count

print("\nEXECUTION SUMMARY")
print("=================")
print("Total Tests:", total_tests)
print("Passed:", pass_count)
print("Failed:", fail_count)

if total_tests > 0:
    pass_percentage = (pass_count / total_tests) * 100
    print("Pass Percentage:", pass_percentage, "%")
