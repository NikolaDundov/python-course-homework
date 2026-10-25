# Homework 1: a loan card
# Run: python 01-intro-syntax-types/homework.py
#
# The fields of loan L000002 come from an Excel export in the Bulgarian format:
# every value is a string, the numbers have a space between the thousands and a
# comma before the decimals. The report date is 30.09.2026.
#
# 1. Convert:  amount, outstanding, rate  -> float
#              days_past_due, maturity_year, report_year -> int
# 2. Calculate:
#      repaid_share     (amount - outstanding) / amount, a float (not rounded)
#      months_left      the whole years from report_year to maturity_year, * 12
#      monthly_payment  the annuity that pays back the outstanding amount in
#                       months_left months:  P * r / (1 - (1 + r) ** -n)
#                       P = outstanding, r = rate / 12 / 100, n = months_left;
#                       rounded to 2 decimals
#      yearly_interest  outstanding * rate / 100 as a Decimal, made from the
#                       cleaned texts and rounded to cents with ROUND_HALF_UP
#      past_due_months, past_due_days  - days_past_due in months of 30 days
#                       and the days left
# 3. card: one string of 8 lines, exactly as in the last check. Each line after
#    the first has the label left in 15 characters, then the value right in 15
#    characters. Build it with f-strings (one per line, joined with "\n", or one
#    f-string in triple quotes). Print it: print(card).
#    Hints: repaid is a percent with 1 decimal; the rate is already in percent
#    (divide it by 100 for the % format, or add the "%" yourself); the value of
#    "past due" is the text "1 m 5 d" - months, "m", days, "d".

import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the repository root, where check.py is
from check import check

loan_id = "L000002"
product = "investment"
amount_text = "1 977 400,00"
outstanding_text = "651 927,30"
rate_text = "5,44"
days_text = "35"
maturity_year_text = "2029"
report_year_text = "2026"

# ---- your code ----
amount = None
outstanding = None
rate = None
days_past_due = None
maturity_year = None
report_year = None

repaid_share = None
months_left = None
monthly_payment = None
yearly_interest = None
past_due_months = None
past_due_days = None

card = None
# ---- end of your code ----

check("amount", amount, 1977400.0)
check("outstanding", outstanding, 651927.3)
check("rate", rate, 5.44)
check("days_past_due", days_past_due, 35)
check("maturity_year", maturity_year, 2029)
check("report_year", report_year, 2026)
check("repaid_share", repaid_share, 0.6703108627490644)
check("months_left", months_left, 36)
check("monthly_payment", monthly_payment, 19667.89)
check("yearly_interest", yearly_interest, Decimal("35464.85"))
check("past_due_months", past_due_months, 1)
check("past_due_days", past_due_days, 5)
check("card", card,
      "Loan L000002 (investment)\n"
      "amount            1,977,400.00\n"
      "outstanding         651,927.30\n"
      "repaid                   67.0%\n"
      "rate                     5.44%\n"
      "interest/year        35,464.85\n"
      "payment/month        19,667.89\n"
      "past due               1 m 5 d")
