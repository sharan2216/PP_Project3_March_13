# Python | Sort Python Dictionaries by Key or Value

myDict = {'ravi': 10, 'rajnish': 9,
          'sanjeev': 15, 'yash': 2, 'suraj': 32}

l=list(myDict.keys())
l.sort()
print(l)

newlist={i:myDict[i] for i in l}
print(newlist)