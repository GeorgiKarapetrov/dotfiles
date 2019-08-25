set = range(2001, 2009)
numDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for y in set :
    isLeap = y % 400 == 0 or ( y % 4 == 0 and y % 100 != 0 )
    print("Year " , y)
    for m in range(0, 12):
        if isLeap and m == 1:
            print(months[m] , " has " , numDays[m]+1 , " days.")
        else:
            print(months[m] , " has " , numDays[m] , " days.")
print("done")