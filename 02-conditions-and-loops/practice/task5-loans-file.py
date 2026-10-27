# Task 5: loop over the rows of a file
# Run: python 02-conditions-and-loops/practice/task5-loans-file.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check, DATA

# == Part 1: totals in one loop ==
# Read data/loans.csv line by line (the starter code opens it and splits each
# line into named fields - all of them are strings). Calculate:
#   count              the number of loans (int)
#   total_outstanding  the sum of outstanding, rounded to 2 decimals (float)
#   stage_3_count      how many loans are in stage 3 (int)
#   usd_count          how many loans are in USD (int)
#   max_days           the largest days_past_due (int)
#   largest_loan_id    the loan_id of the loan with the largest outstanding (str)
#   mortgage_rate      the average interest_rate of the mortgages, rounded to 2
#                      decimals (float) - you need a sum and a count
# Remember to convert: int(days_past_due), float(outstanding), ...

# ---- your code: part 1 ----
count = 0
total_outstanding = 0.0
stage_3_count = 0
usd_count = 0
max_days = 0
largest_loan_id = None
mortgage_rate = None

with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                     # the header
    for line in file:
        (loan_id, client_id, product, currency, start_date, maturity_date,
         amount, outstanding, rate, days_past_due, stage) = line.strip().split(",")
        # your code for each loan
# ---- end of your code ----

check("count", count, 400)
check("total_outstanding", total_outstanding, 131370708.6)
check("stage_3_count", stage_3_count, 19)
check("usd_count", usd_count, 39)
check("max_days", max_days, 200)
check("largest_loan_id", largest_loan_id, "L000070")
check("mortgage_rate", mortgage_rate, 8.04)

# == Part 2: the first loan in stage 3 ==
# In a SECOND loop over the file, find with break:
#   first_stage_3      the loan_id of the first loan in stage 3 (str)

# ---- your code: part 2 ----
first_stage_3 = None
# ---- end of your code ----

check("first_stage_3", first_stage_3, "L000012")
