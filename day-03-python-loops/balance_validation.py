account_balances = [15000, 5000, 20000, 8000, 12000]
tc = [0]
for tc in tc:
  for balance in account_balances:
    if balance >=10000:
      print("TC", tc+1, "- Balance", balance, "- PASS")
    else:
      print("TC", tc+1, "- Balance", balance, "- FAIL")
    tc= tc+1
