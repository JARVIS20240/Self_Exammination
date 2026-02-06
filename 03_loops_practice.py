"""
While Loops:

1. Print all numbers from 1 to 10 using a loop.
2. Print numbers from 10 down to 1 in reverse order.
3. Print all even numbers between 1 and 100.
4. Print all odd numbers between 1 and 100.
5. Print the multiplication table of a given number from n × 1 to n × 10.
6. Calculate and print the sum of the first n natural numbers.
7. Calculate the sum of all even numbers from 1 up to n.
8. Calculate the sum of all odd numbers from 1 up to n.
9. Calculate and print the factorial of a given number.
10. Find and print the product of all digits of a given number.
11. Count and print the total number of digits in a given number.
12. Reverse the given number and print the reversed value.
13. Check whether the given number is a palindrome.
14. Find and print the sum of digits of the given number.
15. Check whether the given number is an Armstrong number.
16. Check whether the given number is a Perfect number.
17. Print all prime numbers between 1 and 100.
18. Check whether the given number is a prime number.
19. Print the Fibonacci series up to n terms.
20. Find and print the sum of the Fibonacci series up to n terms.
21. Print the square of each number from 1 to n.
22. Print the cube of each number from 1 to n.
23. Print all numbers between a and b that are divisible by 7.
24. Print all factors of the given number.
25. Find and print the sum of all factors of the given number.
26. Find the HCF (Highest Common Factor) of two given numbers.
27. Find the LCM (Least Common Multiple) of two given numbers.
28. Find the smallest digit in the given number.
29. Find the largest digit in the given number.
"""

# 1. Print all numbers from 1 to 10 using a loop.
# n =1
# while n <= 10:
#     print(n)
#     n+=1

# 2. Print numbers from 10 down to 1 in reverse order.
# n =10
# while n>=1:
#     print(n)
#     n-=1

# 3. Print all even numbers between 1 and 100.
# n=2
# while n<=100:
#     print(n)
#     n+=2

# 4. Print all odd numbers between 1 and 100.
# n=1
# while n<=100:
#     print(n)
#     n+=2

# 5. Print the multiplication table of a given number from n × 1 to n × 10
# i=1
# n = int(input("Enter Number :"))
# while i<=10:
#     print(f"{n} X {i} = {n*i}")
#     i+=1

# 6. Calculate and print the sum of the first n natural numbers.
# n = int(input("Enter Number :"))
# i=1
# sum=0
# while i<=n:
#     sum += i
#     i+=1
# print(f"Sum = {sum}")

# 7. Calculate the sum of all even numbers from 1 up to n.
# n = int(input("Enter Number :"))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         sum += i
#     i+=1
# print(f"Sum = {sum}")

# 8. Calculate the sum of all odd numbers from 1 up to n.
# n = int(input("Enter Number :"))
# i=1
# sum=0
# while i<=n:
#     if i%2!=0:
#         sum += i
#     i+=1
# print(f"Sum = {sum}")

# 9. Calculate and print the factorial of a given number.
# n = 5
# i = 1 
# fact = 1
# while i<=n:
#     fact *= i
#     i+=1
# print(fact)

# 10. Find and print the product of all digits of a given number.
# n = int(input("Enter number: "))
# product = 1

# while n > 0:
#     digit = n % 10
#     product *= digit
#     n //= 10

# print("Product =", product)

# 11. Count and print the total number of digits in a given number.
# n =123456
# count = 0 

# while n > 0:
#     digit = n % 10
#     count+=1
#     n //= 10

# print(f"count = {count}")

# 12. Reverse the given number and print the reversed value.
# n = 123456
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10

# print(f"Reverse Number= {rev}")

# 11. Count and print the total number of digits in a given number.
n =123456
count = 0 

while n > 0:
    digit = n % 10
    count+=1
    n //= 10

print(f"count = {count}")

# 12. Reverse the given number and print the reversed value.
n = 123456
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(f"Reverse Number= {rev}")

# 13. Check whether the given number is a palindrome.
n = 123
original = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(f"Reverse Number= {rev}")
if original == rev:
    print(f"{original} is palindrome")
else:
    print(f"{original} not palindrome")

# 14. Find and print the sum of digits of the given number.
n = 1234
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n//=10
print(sum)

# 15. Check whether the given number is an Armstrong number.
