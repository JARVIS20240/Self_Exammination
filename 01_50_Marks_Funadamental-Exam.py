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

def check_num():
    try:
        number = int(input("Enter Number: "))
        if (number > 0 ) and (number%2==0):
            print(f"{number} is Positive and Even Number.")
        elif (number > 0 ) and (number%2!=0):
            print(f"{number} is Positive and Odd Number.")
        elif (number < 0):
            print(f"{number} is Negative.")
        else:
            print(f"Zero")

    except ValueError:
        print("Enter Valid Input.")
check_num()