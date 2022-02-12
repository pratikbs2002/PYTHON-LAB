# ID   : 20CE141
# NAME : PRATIK SUTHAR

"""
AIM: You are given n words. Some words may repeat.
     For each word, output its number of occurrences.
     The output order should correspond with the input
     order of appearance of the word.
     See the sample input/output for clarification.

Sample Input
4
bcdef
abcdefg
bcde
bcdef

Sample Output
3
2 1 1

Explanation: There are 3 distinct words. Here, "bcdef"
             appears twice in the input at the first and last positions.
             The other words appear once each. The order of the first
             appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
"""
from collections import Counter  # import Counter from the collections module...

n = int(input())                 # input n for total number of words
word_list = []                   # create list for collect words
for i in range(n):
    word_list.append(input())    # input n words
counter = Counter(word_list)     # counter for count the distinct words in the list
print(len(counter))              # print total number of distinct words
for i in counter:
    print(counter[i], end=' ')   # print the total count of words

