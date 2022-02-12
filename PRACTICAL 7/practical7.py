# ID   : 20CE141
# NAME : PRATIK SUTHAR

"""
Lapindrome is defined as a string which when split in the middle,
gives two halves having the same characters and same frequency
of each character. If there are odd number of characters in
the string, we ignore the middle character and check for lapindrome.
For example gaga is a lapindrome, since the two halves ga and ga have
the same characters with same frequency. Also, abccab, rotor and xyzxy
are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
The two halves contain the same characters but their frequencies do not match.
Your task is simple. Given a string, you need to tell if it is a lapindrome.

Input:
6
gaga
abcde
rotor
xyzxy
abbaab
ababc

Output:
YES
NO
YES
YES
NO
NO

"""
n = int(input())                       # take number of input strings
word_list = []                         # list of input string words

for i in range(n):
    word_list.append(input())          # insert input string into the list

for i in range(0, n):
    input_string = str(word_list[i])   # take input string as a input string from the list
    halve = len(input_string) // 2     # length of the input string divide by 2

    if len(input_string) % 2 == 0:     # check length of the string is even or not
        if sorted(input_string[:halve]) == sorted(input_string[halve:]):
            print('YES')               # print 'YES' if condition true
        else:
            print('NO')
    else:
        if sorted(input_string[:halve]) == sorted(input_string[halve + 1:]):  # check both part are same or not
            print('YES')               # print 'YES' if condition true
        else:
            print('NO')

