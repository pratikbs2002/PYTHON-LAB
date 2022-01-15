# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim : Write a Python program to sum all the items in a dictionary.

Dictionary = {
    '01': 10,
    '02': 20,
    '03': 20,
    '04': 40,
    '05': 50,
    '06': 10,
    '07': 20,
    '08': 30,
    '09': 30,
    '10': 20,
}
Total = 0
for key in Dictionary:
    Total += Dictionary.get(key)

print('Sum : ', Total)
