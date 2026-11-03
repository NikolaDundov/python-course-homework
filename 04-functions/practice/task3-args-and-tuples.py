# Task 3: *args and several return values
# Run: python 04-functions/practice/task3-args-and-tuples.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: a total ==
# total(*amounts)    the sum of any number of amounts; 0 when there are none.
#                    Use a loop (not sum()).

# ---- your code: part 1 ----
def total(*amounts):
    pass
# ---- end of your code ----

check("total(1044231.30, 651927.30, 644.25)", total(1044231.30, 651927.30, 644.25), 1696802.85)
check("total(100)", total(100), 100)
check("total()", total(), 0)

# =============================================================================
# == Part 2: a product ==
# product(*numbers)  the product of any number of numbers: 2, 3, 4 -> 24;
#                    1 when there are none.

# ---- your code: part 2 ----
def product(*numbers):
    pass
# ---- end of your code ----

check("product(2, 3, 4)", product(2, 3, 4), 24)
check("product()", product(), 1)

# =============================================================================
# == Part 3: three results in a tuple ==
# min_max_average(*values)   a tuple of three: the smallest, the largest and the
#                            average of the values, the average rounded to 2.

# ---- your code: part 3 ----
def min_max_average(*values):
    pass
# ---- end of your code ----

check("min_max_average(1, 2, 6)", min_max_average(1, 2, 6), (1, 6, 3.0))

# =============================================================================
# == Part 4: unpack the result ==
# Unpack the result of min_max_average(5.44, 8.83, 4.79, 8.35) into the names
# lowest, highest, average.

# ---- your code: part 4 ----
lowest = highest = average = None
# ---- end of your code ----

check("lowest", lowest, 4.79)
check("highest", highest, 8.83)
check("average", average, 6.85)

# =============================================================================
# == Part 5: months and days ==
# split_days(days_past_due)  a tuple: the whole months of 30 days, and the days
#                            left - 125 -> (4, 5).

# ---- your code: part 5 ----
def split_days(days_past_due):
    pass
# ---- end of your code ----

check("split_days(125)", split_days(125), (4, 5))
check("split_days(30)", split_days(30), (1, 0))

# =============================================================================
# == Part 6: a keyword-only argument ==
# count_over(*values, limit=90)
#     how many values are over the limit; limit can only be given by name
#     (it comes after *values).

# ---- your code: part 6 ----
def count_over(*values, limit=90):
    pass
# ---- end of your code ----

check("count_over(0, 35, 120, 200, 5)", count_over(0, 35, 120, 200, 5), 2)
check("count_over(0, 35, 120, 200, 5, limit=30)", count_over(0, 35, 120, 200, 5, limit=30), 3)
