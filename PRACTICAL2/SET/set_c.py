# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim:- Write a Python program to create an intersection, Union, difference of sets.

set_numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_odd = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
set_even = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print('Intersection of', set_numbers1, 'and', set_even, ' = ', set_numbers1.intersection(set_even))
print('Union of', set_odd, 'and', set_even, ' = ', set_odd.union(set_even))
print('Difference of', set_numbers1, 'From', set_odd, ' = ', set_numbers1.difference(set_odd))

