# Task 3: and / or
# Run: python 02-conditions-and-loops/practice/task3-stage-and-leap-year.py
#
# 1. The IFRS 9 stage of the sample data:
#      stage 3 - more than 90 days past due, or the rating is 10 (default);
#      stage 2 - more than 30 days past due, or the rating is 7 or worse (7, 8, 9);
#      stage 1 - all other loans.
#    Inside the first loop, set stage (an int).
# 2. A year is a leap year (it has 366 days) when it divides by 4 - except the
#    years that divide by 100, which are leap years only if they divide by 400.
#    1900 and 2100 are not leap years, 2000 is. Inside the second loop, set
#    is_leap (True / False) and days (366 or 365). Day counts like ACT/365 and
#    ACT/ACT need this.
#    Hint: "divides by 4" is year % 4 == 0.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

stages = ""
for days_past_due, rating in [(0, 1), (35, 3), (0, 7), (95, 2), (0, 10), (31, 6), (30, 6), (91, 10)]:
    # ---- your code ----
    stage = None
    # ---- end of your code ----
    stages += f"{stage};"

leap_years = ""
day_counts = ""
for year in [2024, 2025, 1900, 2000, 2100, 2028]:
    # ---- your code: part 2 ----
    is_leap = None
    days = None
    # ---- end of your code ----
    leap_years += f"{is_leap};"
    day_counts += f"{days};"

check("stages", stages, "1;2;2;3;3;2;1;3;")
check("leap_years", leap_years, "True;False;False;True;False;True;")
check("day_counts", day_counts, "366;365;365;366;365;366;")
