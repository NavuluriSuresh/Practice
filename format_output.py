import sys
import os

sys.stdout.write("Hello World\n")

name=input("Enter the name of a Person:")
age=float(input("Enter the age of a person:"))

suresh = name
print("my name is {} and I am {} years old".format(name,age))
print("my name is {1} and I am {0} years old".format(name,age))
print("my name is {} and I am {:.2f} years old".format(name,age))

# f-string
print("my name is {0} and I am {1:.2f} years old".format(name,age))

# f-string
print(f"my name is {name} and I am {age} years and {age:.2f} months old")

try:
    print(os.path.getsize(r"D:\Documents\sample.txt"))
    #file handling
    if not os.path.isfile(r"D:\Documents\sample2.txt"):
        raise FileNotFoundError
    with open(r"D:\Documents\sample.txt","x") as f:
        f.write(f"The personal information of {name} is as follows \n")
        f.write(f"my name is {name} and I am {age} years old")
    with open(r"D:\Documents\sample.txt","r") as f:
        print("content of the files sample.txt")
        print(f.read())
except FileExistsError:
    print("File already exists")
except FileNotFoundError:
    print("File not found")
finally:
    print("End of the program")