# . Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.

#     The program should take input from console or args and should handle unexpected inputs    

#     Constraints:

#         - For loop is not allowed

#         - input should be in words:

#             - e.g.: onetwo = 12, sixone = 61

#         - words will be within zero to nine

#         - Cannot use inbuilt methods like max, min, or any math function    

#     Example 1:

#         - Input 1: onezero

#         - Input 2: twozero

#         - Output: onezero

#     Example 2:

#         - Input 1: twosix

#         - Input 2: twofour

#         - Output: two

# dwords = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


lwords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def word_num(num):
        
    i = 0
    while i < 10:
        if lwords[i] in num:
            num = num.replace(lwords[i], str(i))
        i += 1
    return num

def num_word(gcd):

    word_gcd = str(gcd)
    i=0
    while i < 10:
        word_gcd = word_gcd.replace(str(i), lwords[i])
        i += 1
    
    return word_gcd


# def gcd(num1, num2):
#     if num2 == 0:
#         return num1
#     else:
#         return gcd(num2, num1 % num2)

gcd = lambda num1, num2: num1 if num2 == 0 else gcd(num2, num1 % num2)

num1 = input("Number1: ")
num2 = input("Number2: ")

try:
    conv_num1 = int(word_num(num1))
    conv_num2 = int(word_num(num2))
    result = gcd(conv_num1, conv_num2)
    print(f"Result: {num_word(result)}")
except (ValueError, NameError, TypeError) as e:
    print(f"\n\n!!!Please enter the Correct Value!!!\nError: {e}")




