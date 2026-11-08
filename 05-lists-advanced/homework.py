# Homework 5: a list of loans - clean, sort, sum, compare
# Run: python 05-lists-advanced/homework.py
#
# Use the list methods, comprehensions, generator expressions, sorted with key,
# zip and enumerate where they fit. The functions do not print.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the repository root, where check.py is
from check import check, DATA

# =============================================================================
# == Part 1: a watch list ==
# The risk team keeps a list of loan_ids to watch. Change the list watchlist
# itself, with the list methods, in this order:
#   1. remove the first "L000007" (it is in the list twice);
#   2. remove "L000999" - but only if it is in the list;
#   3. add "L000246" at the end;
#   4. sort the list.
# Then:
#   pos_350   the position of "L000350" in the sorted list (index)
watchlist = ["L000120", "L000007", "L000350", "L000007"]

# ---- your code: part 1 ----
pos_350 = None
# ---- end of your code ----

check("watchlist", watchlist, ["L000007", "L000120", "L000246", "L000350"])
check("pos_350", pos_350, 3)

# =============================================================================
# == Part 2: read the loans ==
# read_loans(path)    a list of TUPLES, one per line of the file (without the
#                     header): (loan_id, product, outstanding, days_past_due)
#   The starter code reads the file into rows: one list of texts per line.
#   Take the fields at index 0, 2, 7 and 9 of each row (Python counts from 0:
#   row[0] is loan_id). Convert outstanding with float() and days_past_due
#   with int(). Replace return [] with return [ ... for r in rows] - one
#   comprehension is enough.
#   Parts 3 - 6 use the loans of this part: do it first.

# ---- your code: part 2 ----
def read_loans(path):
    with open(path, encoding="utf-8") as file:
        file.readline()                                     # skip the header
        rows = [line.strip().split(",") for line in file]   # lists of text
    return []
# ---- end of your code ----

loans = read_loans(DATA / "loans.csv")
check("len(loans)", len(loans), 400)
check("loans[2]", loans[2] if loans else None, ("L000003", "credit_card", 644.25, 0))

# =============================================================================
# == Part 3: the largest exposures ==
# top_exposures(loans, n)  the n largest loans by outstanding, as tuples
#                          (rank, loan_id, outstanding), rank from 1
#                          (outstanding is loan[2] in the tuples of part 2)
#   SELECT ... ORDER BY outstanding DESC FETCH FIRST n ROWS ONLY

# ---- your code: part 3 ----
def top_exposures(loans, n):
    return []
# ---- end of your code ----

check("top_exposures(loans, 3)", top_exposures(loans, 3),
      [(1, "L000070", 8999760.03), (2, "L000246", 8675199.12), (3, "L000386", 8073305.05)])

# =============================================================================
# == Part 4: concentration ==
# concentration(loans, n)  the share of the n largest loans in the total
#                          outstanding of all loans, rounded to 4 decimals
#                          (0.4725 = 47.25%): the sum of the n largest divided
#                          by the sum of all. Use top_exposures of part 3.

# ---- your code: part 4 ----
def concentration(loans, n):
    return None
# ---- end of your code ----

check("concentration(loans, 5)", concentration(loans, 5), 0.2952)
check("concentration(loans, 10)", concentration(loans, 10), 0.4725)
check("concentration(loans, 400)", concentration(loans, 400), 1.0)

# =============================================================================
# == Part 5: the late loans ==
# late_summary(loans, days)  a tuple (count, total): how many loans have
#                            days_past_due greater than days, and the sum of
#                            their outstanding rounded to 2 decimals.
#   SELECT COUNT(*), SUM(outstanding) FROM loans WHERE days_past_due > days
# Two generator expressions - no lists.

# ---- your code: part 5 ----
def late_summary(loans, days):
    return None
# ---- end of your code ----

check("late_summary(loans, 90)", late_summary(loans, 90), (17, 4299033.65))
check("late_summary(loans, 0)", late_summary(loans, 0), (54, 9622073.42))
check("late_summary(loans, 10000)", late_summary(loans, 10000), (0, 0))

# =============================================================================
# == Part 6: one product ==
# product_ids(loans, product)  a list of the loan_ids of one product, sorted
#                              by loan_id (A - Z); [] if there are none

# ---- your code: part 6 ----
def product_ids(loans, product):
    return []
# ---- end of your code ----

check("len(product_ids(loans, 'mortgage'))", len(product_ids(loans, "mortgage")), 45)
check("product_ids(loans, 'mortgage')[:2]", product_ids(loans, "mortgage")[:2], ["L000017", "L000040"])
check("product_ids(loans, 'leasing')", product_ids(loans, "leasing"), [])

# =============================================================================
# == Part 7: two years, month by month ==
# month_changes(months, before, after)  tuples (month, change) for each month,
#                                       change = after - before, rounded to 1
#                                       decimal
#   If the three lists do not have the same length, return None: zip would
#   silently drop the months without a pair.

# ---- your code: part 7 ----
def month_changes(months, before, after):
    return []
# ---- end of your code ----

check("month_changes", month_changes(["Jul", "Aug", "Sep"], [128.4, 129.1, 130.2], [129.9, 130.8, 129.7]),
      [("Jul", 1.5), ("Aug", 1.7), ("Sep", -0.5)])
check("month_changes with a missing value", month_changes(["Jul", "Aug"], [128.4, 129.1], [129.9]), None)
