# Flatten a nested list into a single list using a nested list comprehension.

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# flatten = []
# a = [[flatten.append(j) for j in nested_list[i]] for i in range(len(nested_list))]
# print(flatten)

flatten = [j for sublist in nested_list for j in sublist]
print(flatten)