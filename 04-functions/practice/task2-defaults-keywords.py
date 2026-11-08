# Task 2: default values and keyword arguments
# Run: python 04-functions/practice/task2-defaults-keywords.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: the annuity payment ==
# annuity_payment(amount, yearly_rate, years=5)
#   the monthly payment  amount * r / (1 - (1 + r) ** -n), rounded to 2
#   decimals; r = yearly_rate / 12 / 100, n = years * 12.

# ---- your code: part 1 ----
def annuity_payment(amount, yearly_rate, years=5):
    r = yearly_rate / 12 / 100 
    n = years * 12
    return round(amount * r / (1 - (1 + r) ** -n),2)
    
# ---- end of your code ----

check("annuity_payment(20000, 6)", annuity_payment(20000, 6), 386.66)
check("annuity_payment(20000, 6, 10)", annuity_payment(20000, 6, 10), 222.04)

# =============================================================================
# == Part 2: the expected loss ==
# expected_loss(pd_value, ead, lgd=0.45)
#   EL = PD * LGD * EAD, rounded to 2 decimals. 0.45 is the usual LGD of
#   unsecured loans.

# ---- your code: part 2 ----
def expected_loss(pd_value, ead, lgd=0.45):
    return round((pd_value * lgd * ead), 2)
# ---- end of your code ----

check("expected_loss(0.02, 100000)", expected_loss(0.02, 100000), 900.0)

# =============================================================================
# == Part 3: format an amount ==
# format_amount(amount, decimals=2)
#   the amount as text in the Bulgarian format, with `decimals` decimals:
#   format_amount(1044231.3) -> "1 044 231,30", format_amount(1044231.3, 0) ->
#   "1 044 231".
#   Hint: f"{amount:,.{decimals}f}" gives "1,044,231.30" (the number of decimals
#   comes from the parameter), then the two replacements of session 1:
#   text.replace(",", " ").replace(".", ",")

# ---- your code: part 3 ----
def format_amount(amount, decimals=2):
    result = f"{amount:,.{decimals}f}"
    return result.replace(",", " ").replace(".", ",")
# ---- end of your code ----

check("format_amount(1044231.3)", format_amount(1044231.3), "1 044 231,30")
check("format_amount(644.25)", format_amount(644.25), "644,25")
check("format_amount(1044231.3, decimals=0)", format_amount(1044231.3, decimals=0), "1 044 231")

# =============================================================================
# == Part 4: call with keyword arguments ==
# Call your functions with KEYWORD arguments, as in the comments.

# ---- your code: part 4 ----
# the payment of 50000 at 4.5% for 20 years - all three as keyword arguments
def mortgage_payment(amount, yearly_rate, years):
    r = yearly_rate / 12 / 100
    return round(amount * r / (1 - (1 + r) ** - (years * 12)),2) 
#mortgage_payment(amount=50000, yearly_rate=4.5, years=20)

# the expected loss of PD 0.03 and EAD 200000 with LGD 0.25 (a keyword argument)
def secured_el(pd_value, ead, lgd):
    return (pd_value * lgd * ead)

#secured_el(pd_value=0.03, ead=200000, lgd=0.25)
# ---- end of your code ----

check("mortgage_payment", mortgage_payment(amount=50000, yearly_rate=4.5, years=20), 316.32)
check("secured_el", secured_el(pd_value=0.03, ead=200000, lgd=0.25), 1500.0)
