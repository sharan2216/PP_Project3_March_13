def meth():
    str=input("enter a string :")
    mid=int(len(str)/2)
    first_half=str[:mid]
    second_half=str[mid:]

    if first_half==second_half:
        print("symmetrical")
    else:
        print("not symmetrical")

    if first_half==second_half[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


meth()