def meth(s1,s2):
    setlist1.update(setlist2)
    print(setlist1)
    print(setlist1.intersection(setlist2))
    print(setlist1.union(setlist2))


setlist1={"Yellow","Orange"}
setlist2={"Blue","Green","red"}
meth(setlist1,setlist2)