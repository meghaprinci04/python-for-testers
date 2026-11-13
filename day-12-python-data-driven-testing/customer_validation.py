customers = [
    {"name": "Rahul", "status": "ACTIVE", "balance": 15000, "verified": True},
    {"name": "Priya", "status": "ACTIVE", "balance": 5000, "verified": True},
    {"name": "Amit", "status": "INACTIVE", "balance": 20000, "verified": True},
    {"name": "Neha", "status": "ACTIVE", "balance": 25000, "verified": False},
    {"name": "Ravi", "status": "ACTIVE", "balance": 30000, "verified": True}
]
pass_count = 0
fail_count = 0

def validate_customer(status, balance, verified):

    if status == "ACTIVE" and balance >= 10000 and verified:
        return "PASS"
    else:
        return "FAIL"
    
for tc, customer in enumerate(customers, start=1):

    result = validate_customer(
        customer["status"],
        customer["balance"],
        customer["verified"]
    )
    
    print("TC", tc, customer["name"], "-", result)

    if result == "PASS":
        pass_count += 1
    else:
        fail_count += 1
        
total_tests = len(customers)
pass_percentage = (pass_count / total_tests) * 100

print("\nTotal Tests:", total_tests)
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("Pass Percentage:", pass_percentage, "%")


''' Expected Result:

TC 1 Rahul - PASS
TC 2 Priya - FAIL
TC 3 Amit - FAIL
TC 4 Neha - FAIL
TC 5 Ravi - PASS

Total Tests: 5
Pass Count: 2
Fail Count: 3
Pass Percentage: 40.0 %

''''
