
ivr_message = "WELCOME TO ENGLISH BANKING SUPPORT"

# Start validation
if ivr_message.startswith("WELCOME"):
    print("Prompt start validation: PASS")
else:
    print("Prompt start validation: FAIL")

# End validation
if ivr_message.endswith("SUPPORT"):
    print("Prompt end validation: PASS")
else:
    print("Prompt end validation: FAIL")

# Word validation
position = ivr_message.find("ENGLISH")

if position != -1:
    print("English word validation: PASS")
else:
    print("English word validation: FAIL")

print("Word position:", position)

# Case-insensitive comparison
actual_message = "WELCOME TO ENGLISH BANKING SUPPORT"
expected_message = "Welcome to English Banking Support"

if actual_message.lower() == expected_message.lower():
    print("Prompt comparison: PASS")
else:
    print("Prompt comparison: FAIL")
