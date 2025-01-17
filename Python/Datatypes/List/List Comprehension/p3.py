# Given a list of words, create a new list that contains only words with more than 3 characters.

words = ["cat", "dog", "apple", "hi", "tree"]

output = [words[i] for i in range(len(words)) if len(words[i]) > 3]

print(output)