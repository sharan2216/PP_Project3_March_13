# Python program to read character by character from a file
with open("C:/Users/shashi/Desktop/machine learning.txt") as f:
    data=f.readlines()
    for line in data:
        for words in line.split():
            for word in words.split():
                for ch in word.split():
                    print(ch,end='\n')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
# new lines added here
>>>>>>> d1157c6d80cadd921288b8488fdcce55506df1f8



# new lines added here


<<<<<<< HEAD
# new lines added here
>>>>>>> Stashed changes
=======


# new lines added here
>>>>>>> new_branch1
=======
# new lines added here

>>>>>>> d1157c6d80cadd921288b8488fdcce55506df1f8
