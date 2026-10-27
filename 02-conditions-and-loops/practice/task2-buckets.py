# Task 2: if / elif / else
# Run: python 02-conditions-and-loops/practice/task2-buckets.py
#
# 1. The loop below gives days_past_due the values 0, 1, 30, 31, ... one by one.
#    Inside the loop, set bucket to the bucket of the days past due:
#        0          "current"
#        1 - 30     "1-30"
#        31 - 60    "31-60"
#        61 - 90    "61-90"
#        over 90    "90+"
#    Use if / elif / else, and test only one bound in each condition.
# 2. The second loop gives the outstanding amount of a loan last month (old) and
#    this month (new). Set change to "increased", "decreased" or "no change".
#
# Write your code only between the "your code" lines, with the indentation of
# the loop (4 spaces).

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

buckets = ""
for days_past_due in [0, 1, 30, 31, 60, 61, 90, 91, 400]:
    # ---- your code ----
    bucket = None
    # ---- end of your code ----
    buckets += f"{bucket};"

changes = ""
for old, new in [(1000.0, 1200.0), (1000.0, 800.0), (1000.0, 1000.0)]:
    # ---- your code: part 2 ----
    change = None
    # ---- end of your code ----
    changes += f"{change};"

check("buckets", buckets, "current;1-30;1-30;31-60;31-60;61-90;61-90;90+;90+;")
check("changes", changes, "increased;decreased;no change;")
