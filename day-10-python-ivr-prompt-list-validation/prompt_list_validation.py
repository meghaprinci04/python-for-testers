ivr_prompt = ["WELCOME TO BANKING",
"PLEASE ENTER YOUR PIN",
"",
"THANK YOU FOR CALLING"
]
pass_count = 0
fail_count = 0


for tc, prompt in enumerate(ivr_prompt, start=1):
    if prompt.strip() != "":
        print("TC", tc, "- PASS")
        pass_count += 1
    else:
        print("TC", tc, "- FAIL")
        fail_count += 1

total_tests = len(ivr_prompt)
        
print("\nTotal Tests:", total_tests)        
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)


''' Expected Result:
TC 1 - PASS
TC 2 - PASS
TC 3 - FAIL
TC 4 - PASS

Total Tests: 4
Pass Count: 3
Fail Count: 1 '''
