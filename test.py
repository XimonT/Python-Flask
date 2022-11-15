# Python3 implementation of the approach
days = [31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31];
 
# Function to return the day number
# of the year for the given date
def dayOfYear(date):
     
    # Extract the year, month and the
    # day from the date string
    year = (int)(date[0:4]);
    month = (int)(date[5:7]);
    day = (int)(date[8:]);
 
    # If current year is a leap year and the date
    # given is after the 28th of February then
    # it must include the 29th February
    if (month > 2 and year % 4 == 0 and
       (year % 100 != 0 or year % 400 == 0)):
        day += 1;
 
    # Add the days in the previous months
    month -= 1;
    while (month > 0):
        day = day + days[month - 1];
        month -= 1;
    return day;
 
# Driver code
if __name__ == '__main__':
    date = "2020-12-31";
    print(dayOfYear(date));