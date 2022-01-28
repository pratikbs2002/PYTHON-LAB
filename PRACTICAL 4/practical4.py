# ID   : 20CE141
# NAME : PRATIK SUTHAR

"""
Aim:-Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
        You are given n scores. Store them in a list and find the score of the runner-up.

        Input Format:- The first line contains n.
                       The second line contains an array A[]  of n integers each separated by a space.

        Output Format:- Print the runner-up score.

        Sample Input:- 5
                       2 3 6 6 5

        Sample Output:- 5

        Explanation:- Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5.
                      Hence, we print 5 as the runner-up score.
"""

n = int(input())                                                   # take input number of participants
participants_score = list(map(int, input().strip().split()))[:n]   # take a score of participants

pure_score_list = list(set(participants_score))
# first list convert into set therefore all similar score will be remove after that set convert into list.

length_of_pure_list = len(pure_score_list)                         # it is given length of list
sorted_list = sorted(pure_score_list)                              # convert list into the sorted list
print(sorted_list[length_of_pure_list-2])                          # print second largest number (Runner up score)


