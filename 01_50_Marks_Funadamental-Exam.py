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
# nums = [12, 7, 9, 20, 33, 4, 18]
# def seperate_odd_even_num(num):
#     even = []
#     odd = [] 
#     for i in num:
#         if i%2==0:
#             even.append(i)
#         elif i%2!=0:
#             odd.append(i)
#     print((even))
#     print(odd)
#     print(max(even))
#     print(min(odd))
# seperate_odd_even_num(nums)

# 2nd Way:
# nums = [12, 7, 9, 20, 33, 4, 18]

# even_list = [n for n in nums if n%2==0]
# odd_list = [n for n in nums if n%2!=0]

# print(f"Even No. List:{even_list}")
# print(f"Odd No. List:{odd_list}")
# print(f"Largest Even: {max(even_list)}")
# print(f"Smallest Odd: {min(odd_list)}")

# Q4:
"""Create a dictionary of students:

{
  "Aman": 78,
  "Riya": 92,
  "Kunal": 65,
  "Neha": 88
}

Write code to:
Print students scoring above average
Calculate and print the class average
Print the topper’s name and marks"""

# student = {
#             "Aman": 78,
#             "Riya": 92,
#             "Kunal": 65,
#             "Neha": 88  
#             }

# avg = (sum(student.values()) / len(student))
# print(f"Average score: {avg}")

# for name,marks in student.items():
#     if marks > avg :
#         print(f"{name} : {marks}")

# topper_name = max(student, key=student.get)
# topper_marks = student[topper_name]

# print(f"Topper Student= {topper_name} : {topper_marks}")

"""
🔹 Section B — Functions & Problem Solving (10 Marks)
"""
# Q5:
"""
Write a function:
def count_types(data):

Input:

[10, "hi", 3.5, True, None, "Python"]

Output:
Integers: 1
Strings: 2
Floats: 1
Booleans: 1
NoneType: 1
Use correct type checking."""
# def count_types(data):

#     Integers= 0
#     Strings=0
#     Floats=0
#     Booleans= 0
#     NoneType= 0
#     for i in data:
#         if i is None:
#             NoneType+=1
#         elif isinstance(i, bool):
#             Booleans+=1
#         elif isinstance(i, int):
#             Integers+=1
#         elif isinstance(i, str):
#             Strings+=1
#         elif isinstance(i, float):
#             Floats+=1   
#     print("Done")
#     print(f"""
#         Integers: {Integers}
#         Strings: {Strings}
#         Floats: {Floats}
#         Booleans: {Booleans}
#         NoneType: {NoneType}""")
#     print(data)
# data = [10, "hi", 3.5, True, None, "Python"]
# count_types(data)

# Q6:
"""Q6. Error Handling (5 Marks)

Write a program that:
Takes two numbers from user
Divides them
Handles:
Division by zero
Invalid input (non-numeric)
Print meaningful error messages."""
# My code:
# try:
#     a = int(input("Enter 1st Number: "))
#     b = int(input("Enter 2nd Number: "))
#     division = a / b
#     print(division)
# except ValueError:
#     print("Enter valdi Numbers Not Characters.!!!")
# except ZeroDivisionError :
#     print("Not devide by 0")

# Improve Code:
while True:
    try:
        a = float(input("Enter 1st No: "))
        b = float(input("Enter 2nd No: "))
        result = a/b
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    else:
        print(result)
        break
