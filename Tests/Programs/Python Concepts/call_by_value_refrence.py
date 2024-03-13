# call by value
str="geeks"
def meth(str):
    print(str)
    str="greekgod"
    print(str)

meth(str)
print(str)
# call by reference-----

def meth2():

    list.append(22)
    print(list)

list=[1,2,3,4,5]

meth2()
print(list)