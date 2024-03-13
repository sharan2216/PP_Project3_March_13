# Method 1: Use of the index to iterate through the list
# # code
# list = [10, 20, 30, 40, [80, 60, 70]]
# Printing sublist at index 4
# print(list[4])
#
# # Printing 1st element of the sublist
# print(list[4][0])
#
# # Printing 2nd element of the sublist
# print(list[4][1])

# # Printing 3rd element of the sublist
# print(list[4][2])
#
# # Use of Negative Index-----------------------------------
# # Printing sublist at index 4
# print(list[-1])
#
# # Printing 1st element of the sublist
# print(list[-1][-3])
#
# # Printing 2nd element of the sublist
# print(list[-1][-2])
#
# # Printing 3rd element of the sublist
# print(list[-1][-1])
#
# /---------------------------------------------------------------------------------
# How we can iterate through list of tuples in Python--------------------------
#
# create a list of tuples with student
# details
# name = [('sravan', 7058, 98.45),
#         ('ojaswi', 7059, 90.67),
#         ('bobby', 7060, 78.90),
#         ('rohith', 7081, 67.89),
#         ('gnanesh', 7084, 98.01)]
#
# for x in name:
#     for y in x:
#         print(y)
#     print()

# # How to iterate through Excel rows in Python?
# import openpyxl
# wb=openpyxl.load_workbook("C:\\Users\\shashi\\Desktop\\ExcelSheet.xlsx")
# sh=wb['Login']
# max_row=sh.max_row
# max_col=sh.max_column
# data=[]
# for i in range(1,max_row+1):
#     r=[]
#     for j in range(1,max_col+1):
#         r.append((sh.cell(i,j).value))
#     data.append(r)
# print(data)

# Iterate Through Dictionary Keys And Values In Python--------------------------------
# geeks_data = {'language': 'Python', 'framework': 'Django', 'topic': 'Data Structures'}
# # for key,value in geeks_data.items():
# #     print(key,value)
#
# for key in geeks_data.keys():
#     print(key)
# print()
# for value in geeks_data.values():
#     print(value)

# Create a list of dictionaries
languages = [
    {
        "Python": "Machine Learning",
        "R": "Machine learning",
    },
    {
        "Python": "Web development",
        "Java Script": "Web Development",
        "HTML": "Web Development"
    },
    {
        "C++": "Game Development",
        "Python": "Game Development"
    },
    {
        "Java": "App Development",
        "Kotlin": "App Development"
    }
]

# print(languages[0])
# print(languages[1])
# print(languages[2])
# print(languages[3])
for key, val in languages[0].items():
    print("{} : {}".format(key, val))