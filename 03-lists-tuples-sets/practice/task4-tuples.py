# Task 4: tuples as records
# Run: python 03-lists-tuples-sets/practice/task4-tuples.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: unpack a record ==
# Unpack record into the names loan_id, client_id, product, currency,
# outstanding, rate, days_past_due - in one line.
# interest: outstanding * rate / 100, rounded to 2 decimals.
record = ("L000002", "C0132", "investment", "EUR", 651927.30, 5.44, 35)

# ---- your code: part 1 ----

loan_id = record[0]
outstanding = float(record[4])
days_past_due = int(record[-1])
rate = float(record[-2])
interest = round(outstanding * rate / 100 , 2)
# ---- end of your code ----

check("loan_id", loan_id, "L000002")
check("outstanding", outstanding, 651927.30)
check("days_past_due", days_past_due, 35)
check("interest", interest, 35464.85)

# =============================================================================
# == Part 2: a changed copy of a tuple ==
# new_record: the same record, but with days_past_due 40 instead of 35 - a NEW
# tuple, made with a slice and + (a tuple cannot change).

# ---- your code: part 2 ----
new_record = record[:len(record)-1] +(40,)

# ---- end of your code ----

check("new_record", new_record, ("L000002", "C0132", "investment", "EUR", 651927.30, 5.44, 40))
check("record (not changed)", record, ("L000002", "C0132", "investment", "EUR", 651927.30, 5.44, 35))

# =============================================================================
# == Part 3: a tuple with one item ==
# single: a tuple with one item, the string "L000002".

# ---- your code: part 3 ----
single = ("L000002",)
# ---- end of your code ----

check("single", single, ("L000002",))

# =============================================================================
# == Part 4: a list of tuples ==
# loans is a list of tuples (loan_id, product, outstanding, days_past_due).
# With a for loop and unpacking - use new names in the loop, for example
# "for lid, prod, amount, days in loans:", so that you do not overwrite the
# names of part 1:
#   total       the sum of outstanding (rounded to 2 decimals)
#   late_ids    a list of the loan_ids with days_past_due > 0, in order
#   ids, amounts  two lists: all loan_ids, and all outstanding amounts
# And without a loop:
#   last_product  the product of the last loan (two indexes)
loans = [
    ("L000001", "investment", 1044231.30, 0),
    ("L000002", "investment", 651927.30, 35),
    ("L000003", "credit_card", 644.25, 0),
    ("L000014", "consumer", 14286.75, 200),
]

# ---- your code: part 4 ----
late_ids = []
ids = []
amounts = []
total = 0.0

for l in loans:
    for_lid, prod, amount, days_in_loans = l
    total += amount
    ids.append(for_lid)
    amounts.append(amount)
    if days_in_loans > 0:
        late_ids.append(for_lid)

last_product = loans[-1][1]
# ---- end of your code ----

check("total", total, 1711089.6)
check("late_ids", late_ids, ["L000002", "L000014"])
check("ids", ids, ["L000001", "L000002", "L000003", "L000014"])
check("amounts", amounts, [1044231.30, 651927.30, 644.25, 14286.75])
check("last_product", last_product, "consumer")
