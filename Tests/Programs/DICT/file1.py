# initializing string
test_str = "GeeksforGeeks"

# printing original string
print("The original string is : " + test_str)

# creating an empty dictionary
freq = {}

# counting frequency of each character
for char in test_str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# finding the character with maximum frequency
max_char = max(freq, key=freq.get)
min_char = min(freq, key=freq.get)

# printing result
print("The maximum of all characters in GeeksforGeeks is : " + str(max_char))
print("The minimum of all characters in GeeksforGeeks is : " + str(min_char))