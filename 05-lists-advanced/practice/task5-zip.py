# Task 5: lists side by side with zip; a rank with enumerate
# Run: python 05-lists-advanced/practice/task5-zip.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: rows from columns ==
# records    tuples (loan_id, product, outstanding) from the three column
#            lists loan_ids, products, amounts (zip, then list)
loan_ids = ["L000001", "L000002", "L000003"]
products = ["investment", "investment", "credit_card"]
amounts = [1044231.30, 651927.30, 644.25]

# ---- your code: part 1 ----
records = None
# ---- end of your code ----

check("records", records, [("L000001", "investment", 1044231.30), ("L000002", "investment", 651927.30),
                           ("L000003", "credit_card", 644.25)])

# =============================================================================
# == Part 2: a new list from two lists ==
# interest    outstanding * rate / 100 for each loan, rounded to 2 decimals
#             (a comprehension over zip(outstanding, rates))
outstanding = [1044231.30, 651927.30, 644.25]
rates = [8.83, 5.44, 4.79]

# ---- your code: part 2 ----
interest = None
# ---- end of your code ----

check("interest", interest, [92205.62, 35464.85, 30.86])

# =============================================================================
# == Part 3: two years, month by month ==
# changes          the change from 2025 to 2026 for each month (2026 minus
#                  2025), rounded to 1 decimal
# growth_months    the names of the months in which 2026 is larger than 2025
#                  (zip the three lists)
months = ["Jul", "Aug", "Sep", "Oct"]
outstanding_2025 = [128.4, 129.1, 130.2, 131.0]      # EUR million
outstanding_2026 = [129.9, 130.8, 129.7, 131.4]

# ---- your code: part 3 ----
changes = None
growth_months = None
# ---- end of your code ----

check("changes", changes, [1.5, 1.7, -0.5, 0.4])
check("growth_months", growth_months, ["Jul", "Aug", "Oct"])

# =============================================================================
# == Part 4: the shortest list wins ==
# One amount is missing.
#   same_length    True if the two lists have the same length (len)
#   without_pair   the loan_ids that zip drops: the ones after the last amount
#                  (a slice of ids that starts at len(values))
ids = ["L000001", "L000002", "L000003", "L000004"]
values = [800.0, 15900.0, 644.25]

# ---- your code: part 4 ----
same_length = None
without_pair = None
# ---- end of your code ----

check("same_length", same_length, False)
check("without_pair", without_pair, ["L000004"])
check("len(list(zip(ids, values)))", len(list(zip(ids, values))), 3)

# =============================================================================
# == Part 5: a rank ==
# loans: tuples (loan_id, outstanding).
# ranked    the 3 largest loans of loans as tuples (rank, loan_id), rank from
#           1 - sort by the amount from the largest, take 3, then enumerate
#           with start=1
loans = [
    ("L000004", 5875.11),
    ("L000002", 651927.30),
    ("L000003", 644.25),
    ("L000001", 1044231.30),
    ("L000006", 98500.00),
]

# ---- your code: part 5 ----
ranked = None
# ---- end of your code ----

check("ranked", ranked, [(1, "L000001"), (2, "L000002"), (3, "L000006")])
