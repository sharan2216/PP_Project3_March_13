def meth():
    while True:
        n1=int(input("enter 1st num: "))
        n2=int(input("enter 2nd num: "))

        print("1.Add\n 2.Sub\n 3.Mul\n 4.Div\n")
        choice=input("enter ur choice:")
        if choice=='1':
            print(n1+n2)
        elif choice=='2':
            print(n1-n2)
        elif choice=='3':
            print(n1*n2)
        elif choice=='4':
            print(n1/n2)
        else:
            print("Invalid choice")
        ans=input("Do u want to continue? y/n :")
        ans.lower()
        if ans!='y':
            print("Thank you")
            break

meth()