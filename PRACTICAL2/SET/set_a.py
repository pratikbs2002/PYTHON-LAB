# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim:- Write a Python program to add member(s) in a set and clear a set.

set_number = {1, 2, 3}
Check = 'Y'
while Check == 'Y' or Check == 'y':
    element = input("Enter a element you want to add in set : ")
    Check = input("\tPress \'Y\' to add more item : ")
    set_number.add(element)
print(set_number)

Check = input("\tPress \'Y\' to clear a set : ")

if Check == 'Y' or Check == 'y':
    set_number.clear()
print(set_number)
print(len(set_number))
