# str=input("entr a string:")
# s=str.split()
# print(s)
#
# for i in s:
#     # print(len(i))
#     if len(i)//2==0:
#         print(i)
#

#COMPREHEMSION----METHOD-------------
str="geeks for geek is good"
str2=str.split(" ")
print([x for x in str2 if len(x)%2==0])