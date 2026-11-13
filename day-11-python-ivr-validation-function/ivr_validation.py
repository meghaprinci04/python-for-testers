
def validate_prompt(prompt):
    if prompt.strip() != "":
        return "PASS"
    else:
        return "FAIL"


ivr_prompt = [
    "WELCOME TO BANKING",
    "PLEASE ENTER YOUR PIN",
    "",
    "THANK YOU FOR CALLING"
]

pass_count = 0
fail_count = 0

for tc, prompt in enumerate(ivr_prompt, start=1):
    result = validate_prompt(prompt)
    print("TC", tc, "-", result)

    if result == "PASS":
        pass_count += 1
    else:
        fail_count += 1

total_tests = len(ivr_prompt)
pass_percentage = (pass_count / total_tests) * 100

print("\nTotal Tests:", total_tests)
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("Pass Percentage:", pass_percentage, "%")

''' Expected Result

TC 1 - PASS
TC 2 - PASS
TC 3 - FAIL
TC 4 - PASS

Total Tests: 4
Pass Count: 3
Fail Count: 1
Pass Percentage: 75.0 % '''
'''
