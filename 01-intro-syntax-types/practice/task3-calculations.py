# Task 3: calculations with the arithmetic operators
# Run: python 01-intro-syntax-types/practice/task3-calculations.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# == Part 1: the length of this course ==
# This course: 64 academic hours of 40 minutes, in sessions of 4 academic
# hours, and every session has 20 minutes of breaks. Calculate with the
# constants below (do not type the numbers again):
#   sessions      - the number of sessions (int)
#   course_hours  - the length of the course, with the breaks, in hours of
#                   60 minutes (float)
ACADEMIC_HOURS = 64
MINUTES_PER_ACADEMIC_HOUR = 40
ACADEMIC_HOURS_PER_SESSION = 4
BREAK_MINUTES_PER_SESSION = 20

# ---- your code: part 1 ----
sessions = None
course_hours = None
# ---- end of your code ----

check("sessions", sessions, 16)
check("course_hours", course_hours, 48.0)

# == Part 2: days past due in months and days ==
# A loan is 125 days past due. How many months of 30 days, and how many days
# more?  months, days (int) - use // and %
days_past_due = 125

# ---- your code: part 2 ----
months = None
days = None
# ---- end of your code ----

check("months", months, 4)
check("days", days, 5)

# == Part 3: interest ==
# A loan has an outstanding amount of 651927.30 at 5.44% a year.
#   yearly_interest  - outstanding * rate / 100, rounded to 2 decimals
#   monthly_interest - yearly_interest / 12, rounded to 2 decimals
outstanding = 651927.30
rate = 5.44

# ---- your code: part 3 ----
yearly_interest = None
monthly_interest = None
# ---- end of your code ----

check("yearly_interest", yearly_interest, 35464.85)
check("monthly_interest", monthly_interest, 2955.4)

# == Part 4: the monthly payment of a loan ==
# The monthly payment of a loan of 20000 EUR at 6% a year for 5 years
# (an annuity):
#   payment = P * r / (1 - (1 + r) ** -n)
# P is the amount, r the rate of one month (6 / 12 / 100), n the number of
# months. payment rounded to 2 decimals.
loan_amount = 20000
yearly_rate = 6
years = 5

# ---- your code: part 4 ----
payment = None
# ---- end of your code ----

check("payment", payment, 386.66)
