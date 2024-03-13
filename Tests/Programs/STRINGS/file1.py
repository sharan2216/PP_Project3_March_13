# check all vowels in a string----------------
#
# def check(string):
#     # Checking if "aeiou" is a subset of the set of all letters in the string
#     if set("aeiou").issubset(set(string.lower())):
#         return "Accepted"
#     else:
#         return "Not accepted"
#
#
# # Driver code
# if __name__ == "__main__":
#     string = "SEEquoiaL"
#
#     # calling function
#     print(check(string))

# # Python – Least Frequent Character in String--------------------
# str='shashikantsharan'
# n=len(str)
#
# d={}
# for i in str:
#     if i in d:
#         d[i]=d[i]+1
#     else :
#         d[i]=1
#
# res=min(d,key=d.get)
# print(res)

# Python | Maximum frequency character in String
def meth(str):
    d = {}
    for i in str:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    print(d)
    res=max(d,key=d.get)
    print(res)
    res2 = min(d, key=d.get)
    print(res2)


str = "shashikantsharankjdaksh"
meth(str)