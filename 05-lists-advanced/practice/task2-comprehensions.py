# Task 2: derived lists and filters with comprehensions
# Run: python 05-lists-advanced/practice/task2-comprehensions.py
#
# Write ONE list comprehension for each name.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

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
# == Part 1: all ids ==
# ids    all loan_ids, in the order of loans

# ---- your code: part 1 ----
ids = None
# ---- end of your code ----

check("ids", ids, ["L000001", "L000002", "L000003", "L000004", "L000005", "L000006", "L000007"])

# =============================================================================
# == Part 2: a derived column ==
# in_thousands    for each loan, its outstanding / 1000, rounded to 1 decimal
#                 (a list of numbers, in the order of loans)

# ---- your code: part 2 ----
in_thousands = None
# ---- end of your code ----

check("in_thousands", in_thousands, [1044.2, 651.9, 0.6, 5.9, 3.1, 98.5, 12.4])

# =============================================================================
# == Part 3: a filter ==
# late_ids    the loan_ids with days_past_due over 30 (SQL WHERE)

# ---- your code: part 3 ----
late_ids = None
# ---- end of your code ----

check("late_ids", late_ids, ["L000002", "L000005", "L000007"])

# =============================================================================
# == Part 4: CASE WHEN ==
# flags    "late" if days_past_due > 30, else "ok" - one per loan (SQL CASE WHEN)

# ---- your code: part 4 ----
flags = None
# ---- end of your code ----

check("flags", flags, ["ok", "late", "ok", "ok", "late", "ok", "late"])

# =============================================================================
# == Part 5: two conditions, two columns ==
# big_overdrafts    (loan_id, outstanding) tuples of the overdrafts with
#                   outstanding over 5000

# ---- your code: part 5 ----
big_overdrafts = None
# ---- end of your code ----

check("big_overdrafts", big_overdrafts, [("L000004", 5875.11), ("L000007", 12400.0)])

# =============================================================================
# == Part 6: with your own function ==
# buckets    the dpd_bucket of every loan's days_past_due (the function is
#            ready: call it in the comprehension)
def dpd_bucket(days_past_due):
    if days_past_due == 0:
        return "current"
    if days_past_due <= 30:
        return "1-30"
    if days_past_due <= 90:
        return "31-90"
    return "90+"

# ---- your code: part 6 ----
buckets = None
# ---- end of your code ----

check("buckets", buckets, ["current", "31-90", "current", "current", "90+", "1-30", "31-90"])

# =============================================================================
# == Part 7: remove all zeros ==
# remove takes out only the first zero. Make a new list with every amount that
# is not 0, and assign it to amounts again: amounts = [...].
amounts = [0.0, 1200.0, 0.0, 500.0, 0.0]

# ---- your code: part 7 ----

# ---- end of your code ----

check("amounts", amounts, [1200.0, 500.0])
