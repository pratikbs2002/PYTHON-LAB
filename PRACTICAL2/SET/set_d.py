# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim : Write a Python program to find maximum and the minimum value in a set.

set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Without Python In-built Function...
iterator = iter(set_numbers)
first_element = next(iterator, None)
maximum_value = int(first_element)
minimum_value = int(first_element)
for item in set_numbers:
    if item > maximum_value:
        maximum_value = item
    elif item < minimum_value:
        minimum_value = item

print("Without Python In-built Function...")
print('Maximum value : ', maximum_value)
print('Minimum value : ', minimum_value)

# With Python In-built Function...
print("\nWith Python In-built Function...")
print('Maximum value : ', max(set_numbers))
print('Minimum value : ', min(set_numbers))

