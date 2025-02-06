# Fibonacci series
# This code is compatible with python3

# Import required modules

import os
import re
import sys
from time import sleep
import datetime

# Provide the paths to log the output and read the data from files
todays_date=datetime.datetime.time(datetime.datetime.now())
#now().strftime("%Y-%m-%d %H:%M:%S")
print("date is :",todays_date)

# Script Usage

def help():
    return print('''          
    usage:
    <script_name.py> <argument: select any one from the list
    [Fibonacci|Prime]
                 
    ''')

# validations of arguments provided by user
if (len(sys.argv) -1 ) == 1:
    full_cmd_argument=sys.argv
    if full_cmd_argument[1].lower() in ('help','--help','-h'):
        help()
        exit("exiting with help display")
    if full_cmd_argument[1].lower() not in ['fibonacci','prime','factorial']:
        help()
        exit("please provide correct arguments")
    if full_cmd_argument[1].lower() in ('fibonacci','prime'):
        print(full_cmd_argument[1].lower())
    print("full command argument is:",full_cmd_argument)

if (len(sys.argv) -1) != 1:
    help()
    exit("please provide arguments")

num=int(input("enter a number:"))
fiblist=[0,1]
def fibonacci(num):
    global i
    i=0
    while i < num-2 :
        #if isinstance(fiblist,(list,tuple)):
        fiblist.append(fiblist[i]+fiblist[i+1])
        i=i+1

def prime(num):
    start=2
    num1=round(num/2)
    while start < num1:
        rem=num%start
        if rem == 0:
            print(num," is not a prime number")
            break
        start=start+1
        if start == num1 :
            print(num," is a prime number")

def factorial(num): 
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
    #print("The factorial of {} is {}".format(num,fact))

LOG_File = 'output.log'

# Logging the output to a file
if full_cmd_argument[1].lower() == 'fibonacci':
    fibonacci(num)
    with open(LOG_File,'a') as f:
        f.write("The first {} numbers in Fibonacci series is {}\n".format(num,fiblist))
elif full_cmd_argument[1].lower() == 'prime':
    prime(num)
    with open(LOG_File,'a') as f:
        f.write("The {} number is prime number\n".format(num))
elif full_cmd_argument[1].lower() == 'factorial':
    fact = factorial(num)
    with open(LOG_File,'a') as f:
        f.write("The factorial of {} is {}\n".format(num,fact))
else:
    print("please provide correct arguments")
    exit()

print("The output is logged in the file")
sleep(2)
print("exiting the script")
exit()