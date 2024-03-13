# Python – Remove empty List from List-------

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]
print("The original list is : " + str(test_list))
x=[li for li in test_list if li!=[]]
print(x)

