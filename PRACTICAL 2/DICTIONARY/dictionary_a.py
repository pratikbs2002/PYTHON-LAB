# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim : Write a Python script to check whether a given key already exists in a dictionary.

Given_Key = input("Enter a key : ")
Dictionary = {
    'First Name': 'PRATIK',
    'Last Name': 'SUTHAR',
    'Age': 19,
    'Sport': 'CRICKET',
    'Country': 'INDIA',
    'Skills': ['JAVASCRIPT', 'C', 'C++', 'JAVA', 'PYTHON'],
    'Is Married': False,
}
flag_value = 0
for Key in Dictionary:
    if Given_Key == Key:    # Checking key exists in a Dictionary or not...
        print('Given Key Already Exists In A Dictionary.')
        flag_value = 1
        break
if flag_value == 0:  # For printing message that key doesn't exist in a Dictionary...
    print('Given Key Not Exists In A Dictionary.')


