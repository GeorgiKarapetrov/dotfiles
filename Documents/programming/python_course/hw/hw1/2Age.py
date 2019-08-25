import datetime

s = input("Enter your name: ")
name = str(s)

i = input("Enter your age: ")
age = int(i)

currentYear = datetime.datetime.now().year
targetYear = currentYear + 100 - age

print(s, " will be 100 years old in ", targetYear, ".", sep="" )
