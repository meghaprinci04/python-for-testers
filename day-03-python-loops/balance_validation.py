account_balances = [15000, 5000, 20000, 8000, 12000]

for tc, balance in enumerate(account_balances, start=1):
    if balance >= 10000:
        print("TC", tc, "- Balance", balance, "- PASS")
    else:
        print("TC", tc, "- Balance", balance, "- FAIL")
