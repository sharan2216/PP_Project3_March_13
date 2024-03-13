# Python program to read file word by word

with open("C:/Users/shashi/Desktop/machine learning.txt") as f:
    data=f.read()
    for words in data:
        print(words,end='')