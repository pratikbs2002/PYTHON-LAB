def maxArea(a1, length_of_array1):
    area = 0

    for i in range(length_of_array1):
        for j in range(i + 1, length_of_array1):
            area = max(area, min(a1[j], a1[i]) * (j - i))

    return area


a = [int(n) for n in input("Enter an array: ").split()]

length_of_array = len(a)
print(maxArea(a, length_of_array))

print("\nPRATIK SUTHAR : 20CE141")
