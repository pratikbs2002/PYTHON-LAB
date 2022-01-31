# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim : Write a Python script to add a key to a dictionary.

Dictionary = {
    "NAME": "PRATIK SUTHAR"
}
print("\nDictionary : " + str(Dictionary))
Check = 'Y'
print('\nEnter Your Dictionary items : ')
while Check == 'Y' or Check == 'y':
    key = input("\tEnter a Key : ")
    value = input("\tEnter a Value : ")
    Dictionary[key] = value
    Check = input("\tPress \'Y\' to add more item : ")

print("\nDictionary : " + str(Dictionary))
