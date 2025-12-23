# WAP to display number of days in a month.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

month = int(input("Enter the month number (1 for January, 12 for December): "))
year = int(input("Enter the year: "))

# Determine the number of days in the month
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
elif month == 2:
    if is_leap_year(year):
        print("29 days (Leap year)")
    else:
        print("28 days")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
