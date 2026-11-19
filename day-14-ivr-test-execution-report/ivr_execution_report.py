
customers = [
    {"welcome_prompt": "Welcome to help center", "language_selection": "English", "pin_validation": 8275, "balance_enquiry": "Pending transaction", "goodbye_prompt": True},
    {"welcome_prompt": "Welcome to help center", "language_selection": "Hindi", "pin_validation": 8275, "balance_enquiry": "total transaction", "goodbye_prompt": True},
    {"welcome_prompt": "Welcome to help center", "language_selection": "Hindi", "pin_validation": "", "balance_enquiry": "total transaction", "goodbye_prompt": True},
    {"welcome_prompt": "Welcome to help center", "language_selection": "Hindi", "pin_validation": 8275, "balance_enquiry": "total transaction", "goodbye_prompt": True},
    {"welcome_prompt": "Welcome to help center", "language_selection": "Hindi", "pin_validation": 8275, "balance_enquiry": "total transaction", "goodbye_prompt": False}
]

pass_count = 0
fail_count = 0

def validate_customer(welcome_prompt, language_selection,
                      pin_validation, balance_enquiry, goodbye_prompt):

    if not welcome_prompt or not welcome_prompt.strip():
        return "FAIL - Welcome prompt not played"

    elif not language_selection or not language_selection.strip():
        return "FAIL - Language selection failed"

    elif pin_validation is None or str(pin_validation).strip() == "":
        return "FAIL - PIN validation failed"

    elif not balance_enquiry or not balance_enquiry.strip():
        return "FAIL - Balance enquiry failed"

    elif not goodbye_prompt:
        return "FAIL - Goodbye prompt not played"

    else:
        return "PASS"


for tc, customer in enumerate(customers, start=1):

    result = validate_customer(
        customer["welcome_prompt"],
        customer["language_selection"],
        customer["pin_validation"],
        customer["balance_enquiry"],
        customer["goodbye_prompt"]
    )

    print("TC", tc, "IVR Validation", "-", result)

    if result == "PASS":
        pass_count += 1
    else:
        fail_count += 1

total_tests = len(customers)

pass_percentage = (pass_count / total_tests) * 100
fail_percentage = (fail_count / total_tests) * 100

print("\nOverall Execution Summary")
print("-------------------------")
print("Total Tests:", total_tests)
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("Pass Percentage:", pass_percentage, "%")
print("Fail Percentage:", fail_percentage, "%")

if fail_count == 0:
    print("Execution Status: SUCCESS")
else:
    print("Execution Status: COMPLETED WITH FAILURES")


''' Expected Result:
IVR Test Execution Report
Total tests
5

Passed
3

Failed
2

Pass percentage
60%



TC 1 – PASS

TC 2 – PASS

TC 3 – FAIL: PIN validation failed

TC 4 – PASS

TC 5 – FAIL: Goodbye prompt not played
COMPLETED WITH FAILURES'''
