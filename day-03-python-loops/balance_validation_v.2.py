account_balances = [15000, 5000, 20000, 8000, 12000]

pass_count = 0
fail_count = 0

for tc, balance in enumerate(account_balances, start=1):
    if balance >= 10000:
        print("TC", tc, "- Balance", balance, "- PASS")
        pass_count += 1
    else:
        print("TC", tc, "- Balance", balance, "- FAIL")
        fail_count += 1

total_tests = len(account_balances)
pass_percentage = (pass_count / total_tests) * 100

print("Total Tests:", total_tests)
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("Pass Percentage:", pass_percentage, "%")
