# Task 6: while, and a chart with for
# Run: python 02-conditions-and-loops/practice/task6-while.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# == Part 1: how many months to repay a loan ==
# A loan of 15000 EUR at 7.2% a year is repaid with 300 EUR a month. Each
# month: balance = balance + balance * monthly_rate - payment.
# With a while loop, find:
#   months          how many payments are needed (int)
#   total_interest  all payments minus the amount, rounded to 2 decimals.
#                   Careful: the last payment is smaller - when the loop ends,
#                   balance is negative by the part of 300 that was not needed.
amount = 15000.0
monthly_rate = 7.2 / 12 / 100
payment = 300.0

# ---- your code: part 1 ----
months = None
total_interest = None
# ---- end of your code ----

check("months", months, 60)
check("total_interest", total_interest, 2887.41)

# == Part 2: when does a deposit double? ==
# A deposit of 1000 EUR earns 5% a year (deposit = deposit * 1.05 each year).
#   years_to_double  after how many whole years is it 2000 or more? (int)

# ---- your code: part 2 ----
years_to_double = None
# ---- end of your code ----

check("years_to_double", years_to_double, 15)

# == Part 3: a text bar chart ==
# A text bar chart of the number of loans by stage: one "#" for every full 10
# loans (use //). Each line looks like "stage 1 | ##### 58" and ends with "\n".
# Build the whole text in chart, with a for loop over stage_counts.
stage_counts = [(1, 323), (2, 58), (3, 19)]

# ---- your code: part 3 ----
chart = ""
# ---- end of your code ----

check("chart", chart,
      "stage 1 | ################################ 323\n"
      "stage 2 | ##### 58\n"
      "stage 3 | # 19\n")
