
import csv
from io import StringIO

# Sample CSV test data
csv_data = """TC_ID,PIN,Expected
TC01,8275,PASS
TC02,1234,PASS
TC03,ABCD,FAIL
TC04,123,FAIL
TC05,0123,PASS
"""

# Read CSV data
file = StringIO(csv_data) #, I've used StringIO to simulate a CSV file. This avoids needing to upload or create a separate CSV file.
reader = csv.DictReader(file)

total_tests = 0

print("IVR CSV Test Execution")
print("----------------------")

for row in reader:
    print("Test Case:", row["TC_ID"])
    print("PIN:", row["PIN"])
    print("Expected Result:", row["Expected"])
    print("----------------------")

    total_tests += 1

print("Total Test Cases:", total_tests)
