# Task 1: remove, find and sort with the list methods
# Run: python 05-lists-advanced/practice/task1-list-methods.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: remove by value ==
# Remove "L000003" from the list ids (change the list itself, with remove).
ids = ["L000001", "L000002", "L000003", "L000004", "L000005"]

# ---- your code: part 1 ----

# ---- end of your code ----

check("ids", ids, ["L000001", "L000002", "L000004", "L000005"])

# =============================================================================
# == Part 2: remove the last one, and keep it ==
# Remove the last id from ids and keep it in the name last (one method).
# ids is the list after Part 1: do Part 1 first.

# ---- your code: part 2 ----
last = None
# ---- end of your code ----

check("last", last, "L000005")
check("ids", ids, ["L000001", "L000002", "L000004"])

# =============================================================================
# == Part 3: remove only what is there ==
# The loans in closed are repaid. Remove each of them from ids - but only if it
# is in ids (a for loop, an if with in, and remove). "L000009" is not in ids:
# without the if, remove stops with a ValueError. ids is the list after Parts 1
# and 2: do them first.
closed = ["L000002", "L000009"]

# ---- your code: part 3 ----

# ---- end of your code ----

check("ids", ids, ["L000001", "L000004"])

# =============================================================================
# == Part 4: the position of an item ==
# months and outstanding are in the same order. Find the position of "Sep" in
# months (index), and with it the outstanding of September.
#   sep_index         int
#   sep_outstanding   float
months = ["Jul", "Aug", "Sep", "Oct"]
outstanding = [128.4, 129.1, 130.2, 129.6]

# ---- your code: part 4 ----
sep_index = None
sep_outstanding = None
# ---- end of your code ----

check("sep_index", sep_index, 2)
check("sep_outstanding", sep_outstanding, 130.2)

# =============================================================================
# == Part 5: empty a list ==
# The batch is processed: empty the list batch (one method, no new list).
batch = ["L000010", "L000011", "L000012"]

# ---- your code: part 5 ----

# ---- end of your code ----

check("batch", batch, [])

# =============================================================================
# == Part 6: sort() and sorted() ==
#   ascending   a NEW list with the amounts from the smallest (sorted();
#               amounts itself must not change here)
# Then sort amounts itself from the largest (one call of the method sort,
# with reverse=True).
amounts = [5875.11, 651927.30, 644.25, 1044231.30]

# ---- your code: part 6 ----
ascending = None
# ---- end of your code ----

check("ascending", ascending, [644.25, 5875.11, 651927.30, 1044231.30])
check("amounts", amounts, [1044231.30, 651927.30, 5875.11, 644.25])

# =============================================================================
# == Part 7: sort records by a column ==
# loans: tuples (loan_id, product, outstanding).
#   by_product   a NEW list of the loans (the whole tuples), sorted by product
#                (A - Z) - sorted with key
#   top2         the two largest loans by outstanding (ORDER BY outstanding
#                DESC FETCH FIRST 2) - sorted with key and reverse, then a slice
loans = [
    ("L000004", "overdraft", 5875.11),
    ("L000002", "investment", 651927.30),
    ("L000003", "credit_card", 644.25),
    ("L000001", "investment", 1044231.30),
    ("L000006", "mortgage", 98500.00),
]

# ---- your code: part 7 ----
by_product = None
top2 = None
# ---- end of your code ----

check("the products of by_product", [loan[1] for loan in by_product or []],
      ["credit_card", "investment", "investment", "mortgage", "overdraft"])
check("top2", top2, [("L000001", "investment", 1044231.30), ("L000002", "investment", 651927.30)])

# =============================================================================
# == Part 8: the whole record of the smallest loan ==
#   smallest   the loan (the whole tuple) with the smallest outstanding - min
#              with key

# ---- your code: part 8 ----
smallest = None
# ---- end of your code ----

check("smallest", smallest, ("L000003", "credit_card", 644.25))
