
# Day 1 - Python Basics for Testers
# Scenario: Validate customer account status and balance

customer_name = "Megha"
account_status = "ACTIVE"
account_balance = 15000

print("Customer Name:", customer_name)

if account_status == "ACTIVE":
    print("Account Status: PASS")

    if account_balance >= 10000:
        print("Account Balance: PASS")
    else:
        print("Account Balance: FAIL")
else:
    print("Account Status: FAIL")
