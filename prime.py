# Write a Python program to check if a number is a prime number or a palindrome number.

# import packages
import sys
import os
import re

num=int(input("Enter a number:"))
options=str(input("Enter 1:Palindrom 2:Prime 3:Factorial 4:fibonacci:"))
#options=options.lower()

def prime(num):
    if num < 2:
        print(num," is not a Prime number")
        sys.exit(1)
    start=2
    num1=round(num/2)

    while start < num1:
        rem=num%start

        if (rem == 0):
            print(num," is not a prime number")
            break
        start=start + 1
        if (start==num1):
            print(num," is a prime number")

# Palindrome
def palindrome(num):
    #121
    rev=0
    size=len(str(num))
    length=int(size)
    org = num
    while length > 0:
        num1=num%10
        num2=round(num/10)
        rev=rev*10+num1
        num=num2
        length=length-1
    s = (("{} is a Palindrome".format(org)) if org == rev else ("{} is not a Palindrome".format(org)))
    print(s)

# Factorial
def factorial(num):
    for i in range(1,num+1):
        fact=fact*i
        return fact
    
# Fibonacci
def fibonacci(num):
    fiblist=[0,1]
    a=0
    for i in range(0,num-2):
        fiblist.append(fiblist[i]+fiblist[i+1])
        if fiblist[i+2] % 2 == 0:
            a=a+fiblist[i+2]
        i=i+1
    print(fiblist)
    print(f"The sum of even numbers in fibonacci series is: {a}")

def programs(options):
    match options:
        case 1:
            palindrome(num)
        case 2:
            prime(num)
        case 3:
            factorial(num)
        case 4:
            fibonacci(num)
        case _: 
            print("Invalid option, Enter 'palindrome' for palindrome and 'prime' for prime")

if re.findall(r'[^1-9]',options):
    print("Enter only numbers between 1 to 4")
    sys.exit(1)

options=int(options)
if options in (1,2,3,4):
    programs(options)
else:
    print("Invalid option, Enter '1' for palindrome and '2' for prime and '3' for factorial and '4' for fibonacci")
    sys.exit(1)