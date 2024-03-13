# # Reverse tuple-------------
# def meth(tup):
#     tup=tup[::-1]
#     print(tup)
#
# tup=(10,20,30,40,50)
# meth(tup)
#
# #access value 20from tuple----------
# def meth(tup):
#     print(tup[1])
#
# tup=(10,20,30,40,50)
# meth(tup)
#
# #count occurance of tuple 20 from tuple-------
# def meth(tup):
#     print(tup.count(20))
#
# tup=(10,20,30,40,50,20,20)
# meth(tup)
#
# # Tuple unpacking
# Tuple1 = ("Geeks", "For", "Geeks")
# a,b,c=Tuple1
# print(a)
# print(b)
# print(c)

# # Concatenation of tuples
# Tuple1 = (0, 1, 2, 3)
# Tuple2 = ('Geeks', 'For', 'Geeks')
#
# Tuple3=Tuple1+Tuple2
# print(Tuple3)
#

# Tuple1 = tuple('GEEKSFORGEEKS')
#
# # Removing First element
# print("Removal of First Element: ")
# print(Tuple1[1:])
# print(Tuple1[::-1])

# Deleting a Tuple----------------
# Tuples are immutable and hence they do not allow deletion of a part of it.
# The entire tuple gets deleted by the use of del() method.
# Tuple1 = (0, 1, 2, 3, 4)
# del Tuple1
#
# print(Tuple1)
# ----------------------------------------------------------------------

# Python3 program to remove duplicate
# tuples from list of tuples

# def removeDuplicates(lst):
#     return list(set(i for i in lst))
#
#
# lst = [(1, 2), (5, 7), (3, 6), (1, 2)]
# print(removeDuplicates(lst))