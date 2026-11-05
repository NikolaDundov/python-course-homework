# Task 6: sort and find with key and lambda
# Run: python 04-functions/practice/task6-lambda-sorting.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# loans is a list of tuples (loan_id, product, outstanding, interest_rate).
loans = [
    ("L000001", "investment", 1044231.30, 8.83),
    ("L000002", "investment", 651927.30, 5.44),
    ("L000003", "credit_card", 644.25, 4.79),
    ("L000004", "overdraft", 5875.11, 8.35),
    ("L000005", "credit_card", 3127.40, 13.12),
]

# =============================================================================
# == Part 1: the largest first ==
# largest_first   the loan_ids, sorted by outstanding from the largest
#                 (sorted with key=lambda and reverse=True, then collect the ids)

# ---- your code: part 1 ----
largest_first = None
# ---- end of your code ----

check("largest_first", largest_first, ["L000001", "L000002", "L000004", "L000005", "L000003"])

# =============================================================================
# == Part 2: the highest rate ==
# highest_rate    the loan_id of the loan with the highest rate (max with key)

# ---- your code: part 2 ----
highest_rate = None
# ---- end of your code ----

check("highest_rate", highest_rate, "L000005")

# =============================================================================
# == Part 3: sort by two columns ==
# by_product      the loan_ids sorted by product, and inside a product by
#                 loan_id (a key that returns a tuple)

# ---- your code: part 3 ----
by_product = None
# ---- end of your code ----

check("by_product", by_product, ["L000003", "L000005", "L000001", "L000002", "L000004"])

# =============================================================================
# == Part 4: sort ids by their number ==
# ids_by_number   loan ids of different lengths sort wrongly as text
#                 ("L12" < "L3"). Sort short_ids by the NUMBER after the "L":
#                 key=lambda ... int(...[1:])
short_ids = ["L12", "L3", "L100", "L25"]

# ---- your code: part 4 ----
ids_by_number = None
# ---- end of your code ----

check("ids_by_number", ids_by_number, ["L3", "L12", "L25", "L100"])

# =============================================================================
# == Part 5: unique values in order ==
# unique_in_order(items)   a function: a new list without duplicates, in the
#                 order of the first appearance: [3, 1, 3, 2, 1] -> [3, 1, 2]
#                 (set() would lose the order)

# ---- your code: part 5 ----
def unique_in_order(items):
    pass
# ---- end of your code ----

check("unique_in_order([3, 1, 3, 2, 1])", unique_in_order([3, 1, 3, 2, 1]), [3, 1, 2])
check('unique_in_order(["EUR", "USD", "EUR"])', unique_in_order(["EUR", "USD", "EUR"]), ["EUR", "USD"])

# =============================================================================
# == Part 6: loans over a minimum ==
# loans_over(loans, minimum)   a function: the loan_ids with outstanding over
#                 minimum, in the order of loans

# ---- your code: part 6 ----
def loans_over(loans, minimum):
    pass
# ---- end of your code ----

check("loans_over(loans, 5000)", loans_over(loans, 5000), ["L000001", "L000002", "L000004"])
check("loans_over(loans, 10_000_000)", loans_over(loans, 10_000_000), [])
