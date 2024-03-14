# Python program to read character by character from a file
with open("C:/Users/shashi/Desktop/machine learning.txt") as f:
    data=f.readlines()
    for line in data:
        for words in line.split():
            for word in words.split():
                for ch in word.split():
                    print(ch,end='\n')
<<<<<<< Updated upstream
<<<<<<< Updated upstream


# new lines added here
=======
>>>>>>> Stashed changes
=======


# new lines added here
>>>>>>> Stashed changes
