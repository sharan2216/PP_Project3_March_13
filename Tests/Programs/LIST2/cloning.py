# importing copy module
# import copy
# li1 = [1, 2, [3, 5], 4]
# # using copy for shallow copy
# li2 = copy.copy(li1)
# print(li2)

# # 2nd method-------------
# li1 = [4, 8, 2, 10, 15, 18]
# li_copy = li1[:]
# print(li_copy)

# # Python | Count occurrences of an element in a list------------
# l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
# ele=2
# x=[i for i in l if i==ele]
# print(x)
# y=len(x)
# print("element occured for times: ",y)

# 2nd method:---------------
# # Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,countX(lst, x)))


# Python | Remove empty tuples from a list

# Python program to remove empty tuples from a
# list of tuples function to remove empty tuples
# using len()


def Remove(tuples):
    for i in tuples:
        if (len(i) == 0):
            tuples.remove(i)
    return tuples


# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))