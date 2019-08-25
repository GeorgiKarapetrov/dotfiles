x = int ( input("Enter a number: ") )
digits = []

while True:
    digits.append(x % 10)
    x = (x - x % 10)/10
    if(x / 10 < 0.1):
        break    
    
    
sum = 0
for i in digits:
    sum += i
    
print(int(sum))