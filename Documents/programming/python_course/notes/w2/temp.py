NUM_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEK_DAY_NAMES = ["Четвъртък", "Петък", "Събота", "Неделя", 'Понеделник', 'Вторник', 'Сряда']

def isLeap(year):
    return ( year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0 )

def calcNumDaysInMonth(year, month):
    n = NUM_DAYS[month -1]
    if month == 2 and isLeap(year):
        return n+1
    return n

def isValid(date):
    year, month, day = date
    assert type(year) == type(month) == type(day) == int
    if not 1 <= month <= 12:
        return False
    if day < 1 or day > calcNumDaysInMonth(year, month):
        return False
    return True

def enterDate():
    while True:
        year = int( input('Enter a year:') )
        month = int( input('Enter a month:') )
        day = int( input('Enter a day:') )
        date = [year, month, day]
        if isValid(date):
            break
        print('This is not a valid date.')
    return date

def calcNextDate(date):
    assert isValid(date)
    year, month, day = date
    
    if day == calcNumDaysInMonth(year, month):
        nextDay = 1
        nextMonth = month + 1
    else:
        nextDay = day + 1
        nextMonth = month
    if nextMonth == 13:
        nextYear = year + 1
        nextMonth = 1
    else:
        nextYear = year
    return [nextYear, nextMonth, nextDay]

def calcDaysInterval(date1, date2):
    if date1 > date2:
        return -calcDaysInterval(date2, date1)
    
    counter = 0
    while date1 < date2:
        date1 = calcNextDate(date1)
        counter =+ 1
    return counter
        
def calcDayOfWeek(date):
    n = calcDaysInterval([2019, 2, 21], date)
    return WEEK_DAY_NAMES[n % 7]

print( calcDayOfWeek(enterDate()) )