# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim : Write a Python script to merge two Python dictionaries.

# Initialized First Dictionary
Dictionary1 = {
    'First Name': 'PRATIK',
    'Last Name': 'SUTHAR',
    'Age': 19,
   }
# Initialized Second Dictionary
Dictionary2 = {
    'Sport': 'CRICKET',
    'Country': 'INDIA',
    }

print('\nFirst Dictionary : \n\t\t' + str(Dictionary1))  # Printing First Dictionary...
print('Second Dictionary : \n\t\t' + str(Dictionary2))  # Printing Second Dictionary...

Merged_Dictionary = Dictionary1
Merged_Dictionary.update(Dictionary2)

print('\nMerge Dictionary : \n\t\t' + str(Merged_Dictionary))   # Printing Merge Dictionary...
