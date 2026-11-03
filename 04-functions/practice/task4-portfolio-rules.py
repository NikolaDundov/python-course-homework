# Task 4: the rules of the portfolio as functions
# Run: python 04-functions/practice/task4-portfolio-rules.py
#
# The rules of session 2, now as functions that can be used anywhere.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: the days past due bucket ==
# dpd_bucket(days_past_due)   "current" (0), "1-30", "31-90", "90+"
#                             Use return in each branch - no elif needed.

# ---- your code: part 1 ----
def dpd_bucket(days_past_due):
    pass
# ---- end of your code ----

check("dpd_bucket(0)", dpd_bucket(0), "current")
check("dpd_bucket(30)", dpd_bucket(30), "1-30")
check("dpd_bucket(31)", dpd_bucket(31), "31-90")
check("dpd_bucket(91)", dpd_bucket(91), "90+")

# =============================================================================
# == Part 2: the stage ==
# stage(days_past_due, rating)
#     3: more than 90 days or rating 10;
#     2: more than 30 days or rating 7 or worse;
#     1: the rest.

# ---- your code: part 2 ----
def stage(days_past_due, rating):
    pass
# ---- end of your code ----

check("stage(0, 1)", stage(0, 1), 1)
check("stage(35, 3)", stage(35, 3), 2)
check("stage(0, 7)", stage(0, 7), 2)
check("stage(0, 10)", stage(0, 10), 3)
check("stage(91, 2)", stage(91, 2), 3)

# =============================================================================
# == Part 3: the letter grade ==
# grade(rating)    the letter grade of data/rating_scale.csv, with match:
#                  1 AAA, 2 AA, 3 A, 4 BBB, 5 BB, 6 B, 7 CCC, 8 CC,
#                  9 C, 10 D; any other value: "unknown"

# ---- your code: part 3 ----
def grade(rating):
    pass
# ---- end of your code ----

check("grade(1)", grade(1), "AAA")
check("grade(4)", grade(4), "BBB")
check("grade(10)", grade(10), "D")
check("grade(11)", grade(11), "unknown")

# =============================================================================
# == Part 4: investment grade ==
# is_investment_grade(rating)
#     True for the grades BBB and better (rating 1 - 4).
#     Use grade() inside: the grade is in ("AAA", "AA", "A", "BBB").

# ---- your code: part 4 ----
def is_investment_grade(rating):
    pass
# ---- end of your code ----

check("is_investment_grade(4)", is_investment_grade(4), True)
check("is_investment_grade(5)", is_investment_grade(5), False)

# =============================================================================
# == Part 5: the product group ==
# product_group(product)
#     "retail" for mortgage, consumer, credit_card, overdraft; "business" for
#     working_capital, investment, project_finance; "unknown" for anything else.
#     Use a tuple and in, or match.

# ---- your code: part 5 ----
def product_group(product):
    pass
# ---- end of your code ----

check('product_group("overdraft")', product_group("overdraft"), "retail")
check('product_group("project_finance")', product_group("project_finance"), "business")
check('product_group("leasing")', product_group("leasing"), "unknown")
