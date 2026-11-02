account_status = "ACTIVE"
account_balance = 15000
mobile_verification = False

if account_status == "ACTIVE" and account_balance >= 10000 and mobile_verification:
  print("Account is Eligible")
else:
  print("Account is not Eligible")
