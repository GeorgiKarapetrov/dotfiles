while True:
    s = input("Enter a number: ")
    i = int(s)
    if (i % 2 != 0):
        print("This is not an even number. Try again.")
    else:
        break
print(s, "/2 = ", i / 2, sep="")
