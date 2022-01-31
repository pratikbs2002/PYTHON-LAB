# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim : Write a Python program to remove an item from a set if it's present in the set.

set_number = {1, 2, 3, 4, 5}
Check = 'Y'
while Check == 'Y' or Check == 'y':
    random = 0
    element = int(input("Enter a element you want to remove from the set : "))
    for item in set_number:
        if item == element:
            set_number.remove(element)
            print('Element removed successfully...')
            random = 1
            break
    if random == 0:
        print('Element is not exist ')
    Check = input("\tPress \'Y\' to remove more item : ")
    print('\nElements of Set : ', set_number)
