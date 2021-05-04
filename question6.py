# 13021326

""" Implement a function
day_of_year(d, m)
that takes as parameters the number d in the range 1..31 representing a day, and
the number m in the range 1..12 representing a month of the year 2020. It returns
how many complete days passed from the beginning of the fist day of 2020 until the
specified date d/m/2020. Note that 2020 is a leap year, so February has 29 days. The
function must return -1 if the specified date d/m/2020 is not a valid date. Importing
any libraries is NOT allowed.
Indicative test cases:
assert day_of_year(3,1)==2 #must be True
assert day_of_year(10,5)==130 #must be True
assert day_of_year(31,6)==-1 #must be True"""

def correct_date(d, m):
    if d > 31 or d < 1 or m > 12 or m < 1:
        return -1
    else:
        if m == 2 and d > 29:
            return -1
        elif m % 2 == 0 and d > 30:
            return -1
        elif m % 2 == 1 and d > 31:
            return -1
        else:
            return 0

# print(correct_date(3,1))
# print(correct_date(31,6))
# print(correct_date(30,2))

def day_of_year(d, m):
    days_passed = 0
    months_30 = [4, 6, 9, 11]
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    if correct_date(d,m) == -1:
        return -1
    else:
        for i in range(2, m):
            if i in months_31:
                days_passed += 31
            elif i == 2:
                days_passed += 29
            else:
                days_passed += 30
        return days_passed + d - 1


# Indicative test cases:
assert day_of_year(3,1)==2 #must be True
assert day_of_year(10,5)==130 #must be True
assert day_of_year(31,6)==-1 #must be True
