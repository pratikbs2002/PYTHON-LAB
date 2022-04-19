import numpy as np


def procedure_max(list1):
    return np.max(list1)


def procedure_min(list1):
    return np.min(list1)


def procedure_mean(list1):
    return np.mean(list1)


def procedure_standard_deviation(list1):
    return np.std(list1)


def procedure_variance(list1):
    return np.var(list1)


# list1 = [10, 50, 80, 70, 49, 23, 11, 4]

list1 = list(map(int, input().strip().split()))

print(procedure_min(list1))
print(procedure_max(list1))
print(procedure_mean(list1))
print(procedure_standard_deviation(list1))
print(procedure_variance(list1))

