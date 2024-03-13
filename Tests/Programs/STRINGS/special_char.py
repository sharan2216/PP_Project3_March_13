#
# # Program to check if a string contains any special character
#
# str="Geeks$For$Geeks"
# n=len(str)
# str.split()
# count=0
# spe='[@_!#$%^&*()<>?/\|}{~:]'
# for i in range(n):
#     if str[i] in spe:
#         count+=1
# if count:
#     print("string is not accepted")
# else:
#     print("string accepted")


# # Find words which are greater than given length k
# str="My name is shashi sharan and my surname is kant"
# l=str.split()
# k=3
#
# print(l)
# for i in l:
#     if len(i)>=k:
#         print(i)
#

# # Python program for removing i-th character from a string
def remove(str,i):

    a=str[:i]
    b=str[i+1:]
    res=a+b
    print(res)

str="mynameiskant"
remove(str,7)