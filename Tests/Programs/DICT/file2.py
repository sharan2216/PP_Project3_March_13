# Python – Extract Unique values dictionary values


# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# initializing dictionary
from collections import Counter

test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

# # printing original dictionary
# print("The original dictionary is : " + str(test_dict))
#
# valuesList = []
# for key, values in test_dict.items():
#     for value in values:
#         valuesList.append(value)
# freq = Counter(valuesList)
# uniqueValues = list(freq.keys())
# uniqueValues.sort()
#
# # printing result
# print("The unique values list is : " + str(uniqueValues))

# Python program to find the sum of all items in a dictionary

# def dict_sum(myDict):
#     list=[]
#     for i in myDict:
#         print(myDict[i])
#         list.append(myDict[i])
#     final=sum(list)
#     return final
#
# dict={'a':100 , 'b':200 ,'c':300}
# print("sum:",dict_sum(dict))
#
# # Python | Ways to remove a key from dictionary
def diction(myDict):
    # del myDict['b']
    myDict.pop('a')
    print(myDict)



dict={'a':100 , 'b':200 ,'c':300}
diction(dict)