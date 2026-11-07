# Task 2: indexes and slices
# Run: python 03-lists-tuples-sets/practice/task2-slices.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: the parts of a loan id ==
# From loan_id = "L000123", with indexes and slices:
#   prefix      the first character (str)
#   number      the number after it, as an int (123)
loan_id = "L000123"

# ---- your code: part 1 ----
prefix = loan_id[0]
number = int(loan_id[1:])
# ---- end of your code ----

check("prefix", prefix, "L")
check("number", number, 123)

# =============================================================================
# == Part 2: the parts of a date ==
# From report_date = "2026-09-30":
#   year, month, day    as int (2026, 9, 30)
report_date = "2026-09-30"

# ---- your code: part 2 ----
year_num = report_date.split('-')
year = int(year_num[0])
month = int(year_num[1])
day = int(year_num[2])
# ---- end of your code ----

check("year", year, 2026)
check("month", month, 9)
check("day", day, 30)

# =============================================================================
# == Part 3: slices of a year ==
# monthly holds the outstanding amount (in thousands) at the end of each month
# of a year, from January to December. With slices:
#   q1              the first 3 months (a list)
#   q4              the last 3 months
#   quarter_ends    March, June, September, December (every 3rd, from index 2)
#   second_half     July to December
#   without_edges   all months except the first two and the last two
#   newest_first    all months, from December back to January

monthly = [510.0, 505.5, 498.2, 501.0, 495.4, 490.0, 488.8, 480.1, 476.3, 470.0, 468.9, 460.2]

# ---- your code: part 3 ----
q1 = monthly[0:3]
q4 = monthly[9:12]
quarter_ends = monthly[2:12:3]
second_half = monthly[6:]
without_edges = monthly[2:10]
newest_first = monthly[::-1]
# ---- end of your code ----

check("q1", q1, [510.0, 505.5, 498.2])
check("q4", q4, [470.0, 468.9, 460.2])
check("quarter_ends", quarter_ends, [498.2, 490.0, 476.3, 460.2])
check("second_half", second_half, [488.8, 480.1, 476.3, 470.0, 468.9, 460.2])
check("without_edges", without_edges, [498.2, 501.0, 495.4, 490.0, 488.8, 480.1, 476.3, 470.0])
check("newest_first", newest_first, [460.2, 468.9, 470.0, 476.3, 480.1, 488.8, 490.0, 495.4, 501.0, 498.2, 505.5, 510.0])

# =============================================================================
# == Part 4: the last month and the change ==
# last_month: the December value of monthly, with a negative index.
# change: December minus January (a float).

# ---- your code: part 4 ----
last_month = monthly[-1]
change = float(monthly[-1] - monthly[0])
# ---- end of your code ----

check("last_month", last_month, 460.2)
check("change", change, -49.8)

# =============================================================================
# == Part 5: initials ==
# initials: the first letter of each word of "Strategic Risk Analytics",
# joined into one string "SRA" - use split() and a for loop.
team = "Strategic Risk Analytics"

# ---- your code: part 5 ----
l = team.split(" ")
initials =""
for i in l:
    initials += i[0].upper()
print(initials)
# ---- end of your code ----

check("initials", initials, "SRA")
