# def meth(str):
#     l=str.split(' ')
#     print(l)
#     str2='-'.join(l)
#     print(str2)
#
#
# str="Python program to split and join"
# meth(str)

#
# # Python program to find uncommon words from two Strings
# def meth():
#     str1='my name is kant'
#     str2='my sir name is kant'
#     l1=str1.split()
#     print(l1)
#     l2=str2.split()
#     print(l2)
#     l3=[]
#     l4=[]
#     for i in l1:
#         if i not in str2:
#             l3.append(i)
#     for j in l2:
#         if j not in str1:
#             l3.append(j)
#
#     l4=''.join(l3)
#
#     print(l4)
#
#
# meth()


# Python – Replace duplicate Occurrence in String
def meth():
    str1='my name is kant'
    str2='my sir name is kant'
    l1=str1.split()
    print(l1)
    l2=str2.split()
    print(l2)
    l3=[]
    l4=[]
    for i in l1:
        if i in str2 and i not in l3:
            l3.append(i)
    for j in l2:
        if j in str1 and j not in l3:
            l3.append(j)

    l4=' '.join(l3)

    print(l4)


meth()