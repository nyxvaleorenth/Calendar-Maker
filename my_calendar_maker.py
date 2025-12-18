import datetime
from calendar import week

# constants
DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

# get the year
while True:
    print("Please enter the year:")
    response = input("> ")

    if response.isdecimal():
        year = int(response)
        break

# get the month
while True:
    print("Please enter the month 1-12:")
    response = input("> ")

    if response.isdecimal():
        month = int(response)

        if 1 <= month <= 12:
            break
    print("Please enter a number between 1-12")


def getCalendarFor(year, month):
    # store the whole drawing
    calText = ""

    # first row: month and year
    firstRow = " " * 34 + MONTHS[month - 1] + " " + str(year) + "\n"
    calText += firstRow

    # second row: week days
    weekDays = (
        "...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday.."
    )
    calText += weekDays

    return calText


print(getCalendarFor(year, month))
