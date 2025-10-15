print("***** Leap Year Indentifier *****")
year = int(input("Year: \n"))

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False

print("Year " + str(year) + " is " + str(is_leap_year(year)))