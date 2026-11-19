
pin_values = [8275, 1234, "", None, "ABCD", "123"]

pass_count = 0
fail_count = 0

def validate_pin(pin):
    try:
        if pin is None:
            raise TypeError("Missing PIN value")

        pin_text = str(pin)

        if pin_text.isdigit() and len(pin_text) == 4:
            return "PASS"
        else:
            return "FAIL - Invalid PIN format"

    except ValueError:
        return "FAIL - Invalid PIN value"

    except TypeError:
        return "FAIL - Invalid data type"

    finally:
        print("PIN validation completed")


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




''' Expected Result
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
'''

