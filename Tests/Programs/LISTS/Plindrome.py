# #digit 121
#
def palin(num):
    rev=0
    temp=num
    while(num>0):
        dig=num%10
        rev=(rev*10)+dig
        num = num//10
    if (temp==rev):
        print("Palindrome")
    else:
        print("not palindrome")


num=int(input("enter digit :"))
palin(num)

