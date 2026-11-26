
def validate_pin(pin):
    if pin.isdigit() and len(pin) == 4:
        return "PASS"
    else:
        return "FAIL"


pin_values = ["8275", "ABCD", "123", "0123"]

for pin in pin_values:
    result = validate_pin(pin)
    print("PIN:", pin, "-", result)
