# Task 1: first functions
# Run: python 04-functions/practice/task1-first-functions.py
#
# Write the bodies of the functions below. Each one RETURNS its result (no
# print). Replace "pass" with your code. The checks call your functions with
# several values.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: interest ==
# interest(outstanding, rate)    outstanding * rate / 100 (rate is in percent)

# ---- your code: part 1 ----
def interest(outstanding, rate):
    pass
# ---- end of your code ----

check("interest(1000, 5)", interest(1000, 5), 50.0)
check("interest(651927.30, 5.44)", interest(651927.30, 5.44), 35464.84512)

# =============================================================================
# == Part 2: the repaid share ==
# repaid_share(amount, outstanding)
#     the repaid part of the amount: (amount - outstanding) / amount

# ---- your code: part 2 ----
def repaid_share(amount, outstanding):
    pass
# ---- end of your code ----

check("repaid_share(20000, 15000)", repaid_share(20000, 15000), 0.25)
check("repaid_share(800, 800)", repaid_share(800, 800), 0.0)

# =============================================================================
# == Part 3: is the loan late? ==
# is_late(days_past_due)    True when days_past_due is more than 0

# ---- your code: part 3 ----
def is_late(days_past_due):
    pass
# ---- end of your code ----

check("is_late(0)", is_late(0), False)
check("is_late(35)", is_late(35), True)

# =============================================================================
# == Part 4: the monthly rate ==
# monthly_rate(yearly_percent)    the rate of one month as a fraction: 6 -> 0.005

# ---- your code: part 4 ----
def monthly_rate(yearly_percent):
    pass
# ---- end of your code ----

check("monthly_rate(6)", monthly_rate(6), 0.005)
check("monthly_rate(12)", monthly_rate(12), 0.01)

# =============================================================================
# == Part 5: an even number ==
# is_even(number)    True for an even whole number

# ---- your code: part 5 ----
def is_even(number):
    pass
# ---- end of your code ----

check("is_even(4)", is_even(4), True)
check("is_even(5)", is_even(5), False)
