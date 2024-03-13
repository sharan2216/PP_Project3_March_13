# def meth(l):
#     for i in l:
#         print(l[-i],end=' ')
#
# l=[1,2,3,4,5,6]
# meth(l)

# def meth1(l):
#     print(l[::-1])
#
# l=[1,2,3,4,5,6]
# meth1(l)

# def meth2(l):
#     sum=0
#     n=len(l)
#     for i in range(1,n+1):
#         sum=sum+i
#     print(sum)
#
# l=[1,2,3,4,5,6]
# meth2(l)
#
# def meth22(l):
#     sum=1
#     n=len(l)
#     for i in range(1,n+1):
#         sum=sum*i
#     print(sum)
#
# l=[1,2,3,4,5,6]
# meth22(l)


# smallest--------------------------------
# def meth222(l):
#     min=l[0]
#     n=len(l)
#
#     for i in l:
#         if i<min:
#             min=i
#     print(min)
#
# l=[2,3,4,5,6,1]
# meth222(l)

#
# # Python Program to Find Largest Number in a List
# def meth2222(l):
#
#     n=len(l)
#     max = l[-1]
#     for i in l:
#         if i>max:
#             max=i
#     print(max)
#
# l=[11,2,3,4,5,6,1,9]
# meth2222(l)
#
# Python program to find second largest number in a list-----------

# def meth2222(l):
#     l.sort()
#     print(l)
#     print("2nd max is :",l[-2])
#
# l=[11,2,3,4,5,6,1,9]
# meth2222(l)

# Python program to print even numbers in a list-------------
# def meth21(l):
#     num=0
#     even_no=[num for num in l if num%2==0]
#     print(even_no)
#
#
# l=[11,2,3,4,5,6,1,9]
# meth21(l)

# Python program to print all even numbers in a range-----------

# # Python program to print all even numbers  in range
# for even_numbers in range(4, 15, 2):
#     # here inside range function first no denotes starting,
#     # second denotes end and
#     # third denotes the interval
#     print(even_numbers, end=' ')
#
# Python program to print all odd numbers in a range-----------

# Python program to print odd Numbers in given range

start, end = 4, 19
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")