# Task 1: variables and types for one loan
# Run: python 01-intro-syntax-types/practice/task1-first-values.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# == Part 1: the values of one row ==
# The first row of data/loans.csv, as text:
#   L000001,C0080,investment,EUR,2026-01-22,2031-01-22,1156900.00,1044231.30,8.83,0,1
#
# Replace each None with the value from the row, in the right type:
# loan_id and currency are str, outstanding and interest_rate are float,
# days_past_due and stage are int.

# ---- your code: part 1 ----
loan_id = "L000001"
currency = "EUR"
outstanding = 1044231.30
interest_rate = 8.83
days_past_due = 0
stage = 1
# ---- end of your code ----

check("loan_id", loan_id, "L000001")
check("currency", currency, "EUR")
check("outstanding", outstanding, 1044231.30)
check("interest_rate", interest_rate, 8.83)
check("days_past_due", days_past_due, 0)
check("stage", stage, 1)

# == Part 2: is the loan late? ==
# is_late: True when days_past_due is more than 0.

# ---- your code: part 2 ----
is_late = False
# ---- end of your code ----

check("is_late", is_late, False)

# == Part 3: a summary line ==
# summary: an f-string that reads exactly
#   L000001: 1044231.30 EUR at 8.83%

# ---- your code: part 3 ----
summary = "L000001: 1044231.30 EUR at 8.83%"
# ---- end of your code ----

check("summary", summary, "L000001: 1044231.30 EUR at 8.83%")
