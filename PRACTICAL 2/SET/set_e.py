# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim : Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

list_numbers = [2, 4, 6, 'pratik', 'hello']
tuple_numbers = (2, 3, 4, 'pratik')
dictionary_numbers = {1, 2, 3, 'pratik', 'hello'}

set1 = set(list_numbers)
set2 = set(tuple_numbers)
set3 = set(dictionary_numbers)

first_set = set1.intersection(set2)
final_set = set2.intersection(set3)
final_list = list(final_set)
print('Common elements : ', final_list, '\nCounts of Common Numbers : ', len(final_list))

