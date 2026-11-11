customer = {
    "name": "Rahul",
    "account_status": "ACTIVE",
    "balance": 25000,
    "mobile_verified": True,
    "language": "Hindi"
}
customer["balance"] = 30000

print(customer["balance"])

if "mobile_verified" in customer:
    print("Mobile verification details available")
else:
    print("Mobile verification details missing")
    
print(customer["name"])
print(customer["account_status"])
print(customer["balance"])
print(customer["mobile_verified"])
print(customer["language"])

