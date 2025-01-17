# Problem:
# Write a function called is_palindrome(string) that takes a string as input and returns True if the string is a palindrome (reads the same backward as forward), and False otherwise. Ignore case and spaces while checking.

# Example:

# Input: is_palindrome("A man a plan a canal Panama")
# Expected Output: True


def is_palindrome(str):

    
    str = str.lower().replace(" ","")
    str_rev = str[::-1]

    if str != str_rev:
        return False
    else:
        return True


print(is_palindrome("A man a plan a canal Panama"))