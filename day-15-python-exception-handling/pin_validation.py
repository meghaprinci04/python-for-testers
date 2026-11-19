
pin_values = [8275, 1234, "", None, "ABCD", "123"]

pass_count = 0
fail_count = 0

def validate_pin(pin):
    try:
        pin_text = str(pin)

        if pin_text.isdigit() and len(pin_text) == 4:
            return "PASS"
        else:
            return "FAIL"

    except (ValueError, TypeError):
        return "FAIL"


for tc, pin in enumerate(pin_values, start=1):

    result = validate_pin(pin)

    print("TC", tc, "- PIN:", pin, "-", result)

    if result == "PASS":
        pass_count += 1
    else:
        fail_count += 1

print("\nExecution Summary")
print("Total Tests:", len(pin_values))
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)



'''Expected Result
Day 15 execution results
6
Total tests
2
Passed
4
Failed
'''



