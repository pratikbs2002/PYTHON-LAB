# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim:- Write a Python program to add an item in a tuple.

Tuple = ('Pratik', 'Suthar')
Check = 'Y'
while Check == 'Y' or Check == 'y':
    item = input("Enter a item you want to add in tuple : ")
    list1 = list(Tuple)
    list1.append(item)
    Tuple = tuple(list1)
    Check = input("\tPress \'Y\' to add more item : ")

print('Tuple = ' + str(Tuple))
