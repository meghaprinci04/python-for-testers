
ivr_message = "  Welcome to English Banking Support  "

# Step 1: Remove extra spaces
clean_message = ivr_message.strip()

# Step 2: Convert to uppercase
upper_message = clean_message.upper()

# Step 3: Replace English with Hindi
updated_message = upper_message.replace("ENGLISH", "HINDI")

# Step 4: Validate the updated message
if "HINDI" in updated_message:
    print("Prompt validation: PASS")
else:
    print("Prompt validation: FAIL")

print("Final IVR Message:", updated_message)
