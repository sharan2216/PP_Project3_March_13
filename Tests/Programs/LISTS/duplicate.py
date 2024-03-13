# # characters
#
# def meth():
#     str=input("enter string :")
#     dup=[]
#     for i in str:
#         if str.count(i)>1 and i not in dup:
#             dup.append(i)
#     print(dup)
#
# meth()

#words
def meth():
    str=input("enter string :")
    str=str.split()
    # str=''.join(str)
    print(str)
    dup=[]
    for i in str:
        if str.count(i)>1 and i not in dup:
            dup.append(i)
    print(dup)

meth()
