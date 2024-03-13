# # generator:---------
# def meth():
#     for i in range(10):
#         yield i*i
#
#
# a=meth()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# iterator:---------
def meth2():
   l=[1,2,3,4,5]
   newlist = iter(l)
   # newlist=iter([1,2,3,4,5])
   print(next(newlist))
   print(next(newlist))
   print(next(newlist))

meth2()

