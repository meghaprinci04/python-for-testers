
account_balances = [15000, 5000, 20000, 8000, 12000]
statuses = ["ACTIVE", "ACTIVE", "INACTIVE", "ACTIVE", "ACTIVE"]
mobile_verified = [True, True, False, True, True]

pass_count = 0
fail_count = 0

def validate_customer(status, balance, mobile_verified):
    if status == "ACTIVE" and balance >= 10000 and mobile_verified:
        return "PASS"
    else:
        return "FAIL"

for tc, (status, balance, mobile) in enumerate(
    zip(statuses, account_balances, mobile_verified), start=1
):
    result = validate_customer(status, balance, mobile)

    print("TC", tc, "-", result)

    if result == "PASS":
        pass_count += 1
    else:
        fail_count += 1

total_tests = len(account_balances)
pass_percentage = (pass_count / total_tests) * 100

print("\nTotal Tests:", total_tests)
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("Pass Percentage:", pass_percentage, "%")
