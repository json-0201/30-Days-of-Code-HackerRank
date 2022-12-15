# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

r_day, r_month, r_year = list(map(int, input().split()))
d_day, d_month, d_year = list(map(int, input().split()))

date_return = datetime.date(r_year, r_month, r_day)
date_due = datetime.date(d_year, d_month, d_day)

# check for conditions

# if returned on time
if date_return < date_due:
    print(0)

# if returned late but on same month
elif date_return.month == date_due.month:
    print(15 * (date_return.day - date_due.day))

# if returned late but on same year
elif date_return.year == date_due.year:
    print(500 * (date_return.month - date_due.month))

# if returned past the due date's year
else:
    print(10000)
