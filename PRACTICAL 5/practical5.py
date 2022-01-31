# ID   : 20CE141
# NAME : PRATIK SUTHAR
"""
AIM : Swap Case

You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

Sample Input:
            HackerRank.com presents "Pythonist 2".

Sample Output:
            hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""


def Swap_case(x):                       # create one function to swap
    output_string = ""                  # define empty string
    for i in x:
        if i.isupper():                 # if is True when string character is in upper case
            output_string += i.lower()  # convert string character into lower case
        else:                           # when if condition False else will be perform
                                        # here string character is in lower case
            output_string += i.upper()  # convert string character into upper case
    return output_string                # return swapped string


input_string = input()                  # input from user
print(Swap_case(input_string))          # call function and print output
