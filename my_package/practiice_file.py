# from my_package import my_module,my_module1
# my_module.fun1()
# my_module1.fun2()
# from my_package.hello import say_by,say_hi
# say_hi()
# say_by()
# import random
# import string
# print("Generate a random color hex:")
# print("#{:06x}".format(random.randint(0, 0xFFFFFF)))
# print("\nGenerate a random alphabetical string:")
# max_length = 255
# s = ""
# for i in range(random.randint(1, max_length)):
#     s = s+ random.choice(string.ascii_letters)
# print(s)
# print("Generate a random value between two integers, inclusive:")
# print(random.randint(0, 10))
# print(random.randint(-7, 7))
# print(random.randint(1, 1))
# print("Generate a random multiple of 7 between 0 and 70:")
# print(random.randint(0, 10) * 7)
# import random
# import os
# print("Select a random element from a list:")
# elements = [1, 2, 3, 4, 5]
# print(random.choice(elements))
# print(random.choice(elements))
# print(random.choice(elements))
# print("\nSelect a random element from a set:")
# elements = set([1, 2, 3, 4, 5])
# # convert to tuple because sets are invalid inputs
# print(random.choice(tuple(elements)))
# print(random.choice(tuple(elements)))
# print(random.choice(tuple(elements)))
# print("\nSelect a random value from a dictionary:")
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# key = random.choice(list(d))
# print(d[key])
# key = random.choice(list(d))
# print(d[key])
# key = random.choice(list(d))
# print(d[key])
# print("\nSelect a random file from a directory.:")
# print(random.choice(os.listdir("/")))
# import random
# import string
# print("Generate a random alphabetical character:")
# print(random.choice(string.ascii_letters))
# print("\nGenerate a random alphabetical string:")
# max_length = 255
# str1 = ""
# for i in range(random.randint(1, max_length)):
#     str1 += random.choice(string.ascii_letters)
# print(str1)
# print("\nGenerate a random alphabetical string of a fixed length:")
# str1 = ""
# for i in range(10):
#     str1 += random.choice(string.ascii_letters)
# print(str1)
# import random
# print("Construct a seeded random number generator:")
# print(random.Random().random())
# print(random.Random(0).random())
# print("\nGenerate a float between 0 and 1, excluding 1:")
# print(random.random())
# a=20
# b=30
# c=a+b
# print(c)
# d=a*b
# print(d)

"""1: Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the
 product is equal to or lower than 1000. Otherwise, return their sum."""
# def multiplication_or_sum(num1, num2):
#     # calculate product of two number
#     product = num1 * num2
#     # check if product is less then 1000
#     if product <= 1000:
#         return product
#     else:
#         # product is greater than 1000 calculate sum
#         return num1 + num2
#
# # first condition
# result = multiplication_or_sum(20, 30)
# print("The result is", result)
#
# # Second condition
# result = multiplication_or_sum(40, 30)
# print("The result is", result)

"""2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration,
 print the sum of the current and previous number."""
# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0
#
# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i

"""3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display 
characters that are present at an even index number."""
# # accept input string from a user
# word = input('Enter word ')
# print("Original String:", word)
#
# # get the length of a string
# size = len(word)
#
# # iterate a each character of a string
# # start: 0 to start with first character
# # stop: size-1 because index starts with 0
# # step: 2 to get the characters present at even index like 0, 2, 4
# print("Printing only even index chars")
# for i in range(0, size - 1, 2):
#     print("index[", i, "]", word[i])
# accept input string from a user
# word = input('Enter word ')
# print("Original String:", word)
#
# # using list slicing
# # convert string to list
# # pick only even index chars
# x = list(word)
# for i in x[0::2]:
#     print(i)
"""4: Remove first n characters from a string
Write a program to remove characters from a string 
starting from zero up to n and return a new string."""
# def remove_chars(word, n):
#     print('Original string:', word)
#     x = word[n:]
#     return x
#
# print("Removing characters from a string")
# print(remove_chars("ASHOK", 4))
# print(remove_chars("ASHOK", 2))
"""5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a
given list is same. If numbers are different then return False"""
'''given data:
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]'''


# def first_last_same(numberList):
#     print("Given list:", numberList)
#
#     first_num = numberList[0]
#     last_num = numberList[-1]
#
#     if first_num == last_num:
#         return True
#     else:
#         return False
#
#
# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))
#
# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))
"""6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only 
those numbers which are divisible by 5"""
# num_list = [10, 20, 33, 46, 55]
# print("Given list:", num_list)
# print('Divisible by 5:')
# for num in num_list:
#     if num % 5 == 0:
#         print(num)
"""7: Return the count of a given substring from a string
Write a program to find how many times substring “Ashok” appears in the given string."""
# str_x = "Ashok is good developer. Ashok is a writer"
# # use count method of a str class
# cnt = str_x.count("Emma")
# print(cnt)
# def count_ashok(statement):
#     print("Given String: ", statement)
#     count = 0
#     for i in range(len(statement) - 1):
#         count += statement[i: i + 4] == 'Ashok'
#     return count
#
# count = count_ashok("Ashok is good developer. Ashok is a writer")
# print("Ashok appeared ", count, "times")
"""8: Print the following pattern"""
# for num in range(10):
#     for i in range(num):
#         print (num,end="0") #print number
#     # new line after each row to display pattern correctly
#     print("\n")
"""9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse.
 For example, 545, is the palindrome numbers"""
# def palindrome(number):
#     print("original number", number)
#     original_num = number
#     # reverse the given number
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10
#     # check numbers
#     if original_num == reverse_num:
#         print("Given number palindrome")
#     else:
#         print("Given number is not palindrome")
# palindrome(121)
# palindrome(125)


""" 10: Create a new list from two list using the following condition
Create a new list from two list using the following condition
Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
Given:
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]  """
# def merge_list(list1, list2):
#     result_list = []
#     # iterate first list
#     for num in list1:
#         # check if current number is odd
#         if num % 2 != 0:
#             # add odd number to result list
#             result_list.append(num)
#     # iterate second list
#     for num in list2:
#         # check if current number is even
#         if num % 2 == 0:
#             # add even number to result list
#             result_list.append(num)
#     return result_list
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print("result list:", merge_list(list1, list2))
"""11: Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“,
 with a space separating the digits."""
# number = 7536
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")
"""12: Calculate income tax for the given income by adhering to the rules below
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20"""
# income = 45000
# tax_payable = 0
# print("Given income", income)
# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # no tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_payable = x * 10 / 100
# else:
#     # first 10,000
#     tax_payable = 0
#     # next 10,000 10% tax
#     tax_payable = 10000 * 10 / 100
#     # remaining 20%tax
#     tax_payable += (income - 20000) * 20 / 100
# print("Total tax to pay is", tax_payable)

"""13: Print multiplication table from 1 to 10"""
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print("\t\t")
"""14: Print a downward Half-Pyramid Pattern of Star (asterisk)"""
# for i in range(6, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")
"""15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.
"""
# def exponent(base, exp):
#     num = exp
#     result = 1
#     while num > 0:
#         result = result * base
#         num = num - 1
#     print(base, "raises to the power of", exp, "is: ", result)
# exponent(5, 4)








