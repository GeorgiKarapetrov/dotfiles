#exceptions.py

while True:
    try:
        age = int(input("Enter your age: "))
        print(age)
    except ValueError:
        print("Invalid number")

