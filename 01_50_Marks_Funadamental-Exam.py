# 1st Paper:
"""
🔹 Section A — Python Fundamentals (20 Marks)
"""
# Q1: 
"""Q1. Input, Conditions, Logic (5 Marks)
Write a program that:
Takes an integer input n

Prints:
"Positive Even" if n is positive and even
"Positive Odd" if n is positive and odd
"Negative" if n is negative
"Zero" if n == 0
📌 Marks Deduction if logic is repetitive or poorly structured."""

# def check_num():
#     try:
#         number = int(input("Enter Number: "))
#         if (number > 0 ) and (number%2==0):
#             print(f"{number} is Positive and Even Number.")
#         elif (number > 0 ) and (number%2!=0):
#             print(f"{number} is Positive and Odd Number.")
#         elif (number < 0):
#             print(f"{number} is Negative.")
#         else:
#             print(f"Zero")

#     except ValueError:
#         print("Enter Valid Input.")
# check_num()

# Q2
"""Q2. Loops & Number Logic (5 Marks)

Write a program to:
Take a number n
Reverse the number
Check whether the reversed number is palindrome"""

# def Palindrome():
#         try:
#             number = int(input("Enter Number:"))
#             if number <0 :
#                 print("Negative numbers are not considered Palindrome.")
#                 return
            
#             rev_num = int(str(number)[::-1])
            
#             print(f"Entered number: {number}\nReverse Number: {rev_num}")

#             if (number == rev_num):
#                 print(f"{number} is Palindrome.")
#             else:
#                 print(f"{number} not Palindrome.")
#         except ValueError:
#              print("Entere valid input.")
# Palindrome()

# Q3:
"""Given a list:
nums = [12, 7, 9, 20, 33, 4, 18]

Write code to:
Separate even and odd numbers into two lists
Find the largest even number
Find the smallest odd number
Print all results clearly."""
nums = [12, 7, 9, 20, 33, 4, 18]
def seperate_odd_even_num(num):
    even = []
    odd = [] 
    for i in num:
        if i%2==0:
            even.append(i)
        elif i%2!=0:
            odd.append(i)
    print((even))
    print(odd)
    print(max(even))
    print(min(odd))
seperate_odd_even_num(nums)