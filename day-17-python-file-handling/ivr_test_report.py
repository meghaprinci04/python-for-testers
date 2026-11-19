

test_results = """
PIN validation completed
TC 1 - PIN: 8275 - PASS
PIN validation completed
TC 2 - PIN: 1234 - PASS
PIN validation completed
TC 3 - PIN:  - FAIL - Invalid PIN format
PIN validation completed
TC 4 - PIN: None - FAIL - Invalid data type
PIN validation completed
TC 5 - PIN: ABCD - FAIL - Invalid PIN format
PIN validation completed
TC 6 - PIN: 123 - FAIL - Invalid PIN format

Execution Summary
Total Tests: 6
Pass Count: 2
Fail Count: 4
"""

with open("ivr_test_report.txt", "w") as file:
    file.write(test_results)

print("Test report saved successfully!")

with open("ivr_test_report.txt", "r") as file:
    report_content = file.read()

print("\nSaved IVR Test Report:")
print(report_content)
