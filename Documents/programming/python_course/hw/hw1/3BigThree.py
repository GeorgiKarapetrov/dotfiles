x = float ( input("Enter a number: ") )
y = float ( input("Enter a number: ") )
z = float ( input("Enter a number: ") )

if x > y:
    bigger = x
else:
    bigger = y
if bigger > z:
    print ( "The maximum of", x,y,z, "is", bigger)
else:
    print ( "The maximum of", x,y,z, "is", z)
    #check for int type, etc