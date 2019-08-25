x = int ( input("Enter a number: ") )
list = [11, 99, 1, 2, 39, 5, 8, 13, 21, 4, 55, 89]
final = []
for i in list:
    if i < x:
        final.append(i)
print(final)