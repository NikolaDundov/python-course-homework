# Task 4: sums and counts with a condition, without a list
# Run: python 05-lists-advanced/practice/task4-generators.py
#
# Do not build a list: use ONE generator expression inside sum / max for each
# name - sum(x for ... if ...), sum(1 for ... if ...).

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check, DATA

# loans is a list of tuples (loan_id, product, currency, outstanding, days_past_due).
loans = [
    ("L000001", "investment", "EUR", 1044231.30, 0),
    ("L000002", "investment", "EUR", 651927.30, 35),
    ("L000003", "credit_card", "EUR", 644.25, 0),
    ("L000004", "overdraft", "EUR", 5875.11, 0),
    ("L000005", "overdraft", "USD", 3127.40, 120),
    ("L000006", "mortgage", "USD", 98500.00, 15),
    ("L000007", "overdraft", "EUR", 12400.00, 60),
]

# =============================================================================
# == Part 1: SUM ==
# total    the sum of outstanding of all loans, rounded to 2 decimals

# ---- your code: part 1 ----
total = None
# ---- end of your code ----

check("total", total, 1816705.36)

# =============================================================================
# == Part 2: SUM ... WHERE ==
# usd_total    the sum of outstanding of the USD loans (not rounded)

# ---- your code: part 2 ----
usd_total = None
# ---- end of your code ----

check("usd_total", usd_total, 101627.4)

# =============================================================================
# == Part 3: COUNT(*) ... WHERE ==
# late_count    how many loans have days_past_due > 30

# ---- your code: part 3 ----
late_count = None
# ---- end of your code ----

check("late_count", late_count, 3)

# =============================================================================
# == Part 4: MAX ... WHERE ==
# largest_overdraft    the largest outstanding of the overdrafts (max)

# ---- your code: part 4 ----
largest_overdraft = None
# ---- end of your code ----

check("largest_overdraft", largest_overdraft, 12400.0)

# =============================================================================
# == Part 5: a file, one line at a time ==
# file_total    the sum of outstanding of all loans in loans.csv, rounded to
#               2 decimals. outstanding is at index 7 of a line split by
#               "," (Python counts from 0: line.split(",")[7]); it is text,
#               so convert it with float(). Do not read the file into a list:
#               sum( ... for line in file) reads it one line at a time. The
#               starter code opens the file and skips the header; replace
#               None with the sum, inside the with block.

# ---- your code: part 5 ----
with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                  # skip the header
    file_total = None
# ---- end of your code ----

check("file_total", file_total, 131370708.6)

# =============================================================================
# == Part 6: COUNT in a file ==
# stage3_count    how many loans in loans.csv are in stage 3. stage is the last
#                 column, index 10 (counting from 0); it is text: compare with
#                 "3". Watch out: the last field of a line ends with "\n" -
#                 strip the line first. Replace None, inside the with block.

# ---- your code: part 6 ----
with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                  # skip the header
    stage3_count = None
# ---- end of your code ----

check("stage3_count", stage3_count, 19)
