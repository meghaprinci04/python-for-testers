
account_balances = [15000, 5000, 20000, 8000, 12000]

pass_count = 0
fail_count = 0

# Function to validate one account balance
def validate_balance(balance):
    if balance >= 10000:
        return "PASS"
    else:
        return "FAIL"


# Execute all test cases
for tc, balance in enumerate(account_balances, start=1):

    result = validate_balance(balance)

    if result == "PASS":
        print("TC", tc, "- Balance", balance, "-", result)
        pass_count += 1
    else:
        print("TC", tc, "- Balance", balance, "-", result)
        fail_count += 1


# Execution summary
total_tests = len(account_balances)
pass_percentage = (pass_count / total_tests) * 100

print("\nTotal Tests:", total_tests)
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("Pass Percentage:", pass_percentage, "%")
