# def meth(l):
#     l[0],l[-1]=l[-1],l[0]
#     print(l)
#
# l=[1,2,3,4,5]
# meth(l)

# def meth2(l1):
#     i=6
#     if i in l1:
#         print("exist")
#     else:
#         print("not exist")
#
# l1=[ 1, 6, 3, 5, 3, 4 ]
# meth2(l1)

# clear a list------------------
# def meth3(l):
#     print("before clear:",l)
#     l.clear()
#     print(l)
#
# l=[ 1, 6, 3, 5, 3, 4 ]
# meth3(l)

def meth33(l):
    print("before clear:",l)
    del(l[:])
    print(l)

l=[ 1, 6, 3, 5, 3, 4 ]
meth33(l)