def char_frequency(input_string1):
    dictionary1 = {}
    for n in input_string1:
        keys = dictionary1.keys()

        if n in keys:
            dictionary1[n] += 1
        else:
            dictionary1[n] = 1

    return dictionary1


input_string = input("Enter a string: ")
print(char_frequency(input_string))


print("\nPRATIK SUTHAR : 20CE141")
