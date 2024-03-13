# list comprehension:-----
l=[i for i in range(1,10) if i%2]
print(l)

#dictionary comprehension---------
d={i:i*i for i in range(10)}
print(d)

#set comprehension---------
s={i for i in range(10) if i%2==0}
print(s)

#tuple comprehension---------