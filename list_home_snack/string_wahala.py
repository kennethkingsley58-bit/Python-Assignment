words = input("Enter words: ")
words = words.split()

count = 0
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count = count + 1
print("Amount of words: ", count)
