# Write a Python program to check if a number is a prime number or a palindrome number.

# import packages
import sys
import os
import re

num=int(input("Enter a number:"))
options=str(input("Enter palindorm for palindrome and prime for prime:"))
options=options.lower()

def prime(num):
    if num == 1:
        print(num," is not a Prime number")
    if num == 2:
        print(num," is a Prime number")
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

def programs(options):
    match options:
        case 'palindrome':
            palindrome(num)
        case 'prime':
            prime(num)
        case _: 
            print("Invalid option, Enter 'palindrome' for palindrome and 'prime' for prime")

if re.findall(r'[^a-zA-Z]',options):
    print("Enter only alphabets")
    sys.exit(1)

if options == 'palindrome' or options == 'prime':
    programs(options)
else:
    print("Invalid option, Enter 'palindrome' for palindrome and 'prime' for prime")
    sys.exit(1)