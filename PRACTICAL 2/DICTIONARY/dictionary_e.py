# ID   : 20CE141
# NAME : PRATIK SUTHAR

# Aim : Write a Python script to concatenate following dictionaries to create a new one:
#           Sample Dictionary:-
#                 dic1 = {1:10, 2:20}
#                 dic2 = {3:30, 4:40}
#                 dic3 = {5:50, 6:60}
#
#           Expected Result : {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

print("dic1 = " + str(dic1))
print("dic2 = " + str(dic2))
print("dic3 = " + str(dic3))

merged_dic = dic1
merged_dic.update(dic2)
merged_dic.update(dic3)
print("Merged dic = " + str(merged_dic))


