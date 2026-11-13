
ivr_message = "WELCOME TO ENGLISH BANKING SUPPORT"

actual_message = "WELCOME TO ENGLISH BANKING SUPPORT"
expected_message = "Welcome to English Banking Support"

# TC01: Prompt start validation
if ivr_message.startswith("WELCOME"):
    print("TC01 - Prompt start validation: PASS")
else:
    print("TC01 - Prompt start validation: FAIL")

# TC02: Prompt ending validation
if ivr_message.endswith("SUPPORT"):
    print("TC02 - Prompt ending validation: PASS")
else:
    print("TC02 - Prompt ending validation: FAIL")

# TC03: Word existence validation
position = ivr_message.find("ENGLISH")

if position != -1:
    print("TC03 - English keyword validation: PASS")
else:
    print("TC03 - English keyword validation: FAIL")

print("Word position:", position)

# TC04: Case-insensitive message comparison
if actual_message.lower() == expected_message.lower():
    print("TC04 - Message comparison: PASS")
else:
    print("TC04 - Message comparison: FAIL")


''' Expected Result:
TC01 - Prompt start validation: PASS
TC02 - Prompt ending validation: PASS
TC03 - English keyword validation: PASS
Word position: 11
TC04 - Message comparison: PASS '''
