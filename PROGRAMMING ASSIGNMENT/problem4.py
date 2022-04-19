from itertools import combinations

num = [int(n) for n in input("Enter element: ").split()]

k = int(input("Enter the value of K : "))
count_variable = 0

for i in range(1, len(num) + 1):

    for c in combinations(num, i):
        if sum(c) == k:
            count_variable += 1

print(count_variable)

print("\nPRATIK SUTHAR : 20CE141")
