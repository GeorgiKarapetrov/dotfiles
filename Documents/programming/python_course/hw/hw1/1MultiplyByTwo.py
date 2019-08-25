while True:
    s = input("Enter a number: ")
    i = float(s)
    if type(i) is not float:
        print("This is not a number. Try again.")
        continue

    # check if int
    if i - i // 1 == 0:
        print(s, "multiplied by two is", int(i) * 2)
    else:
        print(s, "multiplied by two is", i * 2)
    break
