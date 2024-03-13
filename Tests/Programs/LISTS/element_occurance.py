# def meth(l):
#     count=0
#     x=int(input("enter the value :"))
#     for i in l:
#         if i==x:
#             count=count+1
#     print(count)
#
#
# l=[1,2,1,3,4,5,3,6,7,8,9,1,1]
# meth(l)

#delete 1st element of the list:---------
def meth(l):
    # --deletes last element
    l.pop()

    # --deletes 1st element
    l.pop(0)

    # --deletes specific element
    l.pop(5)
    print(l)

l=[1,2,1,3,4,5,3,6,7,8,9]
meth(l)