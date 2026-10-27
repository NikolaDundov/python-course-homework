# Homework 2: a report of days past due
# Run: python 02-conditions-and-loops/homework.py
#
# Read data/loans.csv (as in task 5) and put every loan into one of four buckets
# by its days_past_due: "current" (0), "1-30", "31-90", "90+".
#
# 1. For each bucket, the number of loans and the sum of outstanding:
#      current_count, late_30_count, late_90_count, over_90_count       (int)
#      current_total, late_30_total, late_90_total, over_90_total       (float,
#      rounded to 2 decimals after the loop)
# 2. total: the sum of all outstanding, rounded to 2 decimals;
#    over_90_share: over_90_total / total, rounded to 4 decimals.
# 3. The largest LATE loan (days_past_due > 0) by outstanding:
#      largest_late_id (str), largest_late_amount (float), largest_late_days (int)
# 4. report: one string of 6 lines, exactly as in the last check: a header,
#    one line per bucket, and a total line. Each line: the bucket name left in 8
#    characters, the count right in 6, the outstanding right in 18 with a thousands
#    separator and 2 decimals, the share right in 8 as a percent with 1 decimal.
#    The lines are joined with "\n" (no "\n" at the end). Print it.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the repository root, where check.py is
from check import check, DATA

# ---- your code ----
current_count = late_30_count = late_90_count = over_90_count = 0
current_total = late_30_total = late_90_total = over_90_total = 0.0
total = None
over_90_share = None
largest_late_id = None
largest_late_amount = None
largest_late_days = None
report = None
# ---- end of your code ----

check("current_count", current_count, 346)
check("late_30_count", late_30_count, 28)
check("late_90_count", late_90_count, 9)
check("over_90_count", over_90_count, 17)
check("current_total", current_total, 121748635.18)
check("late_30_total", late_30_total, 3279532.15)
check("late_90_total", late_90_total, 2043507.62)
check("over_90_total", over_90_total, 4299033.65)
check("total", total, 131370708.6)
check("over_90_share", over_90_share, 0.0327)
check("largest_late_id", largest_late_id, "L000103")
check("largest_late_amount", largest_late_amount, 1237517.53)
check("largest_late_days", largest_late_days, 200)
check("report", report,
      "bucket   loans       outstanding   share\n"
      "current    346    121,748,635.18   92.7%\n"
      "1-30        28      3,279,532.15    2.5%\n"
      "31-90        9      2,043,507.62    1.6%\n"
      "90+         17      4,299,033.65    3.3%\n"
      "total      400    131,370,708.60  100.0%")
