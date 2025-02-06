# Program is to identify whether the gi en year is Leap year or not

y=int(input("Enter the Year:"))
if (y%4==0 and y%100!=0) or (y%400==0):
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")