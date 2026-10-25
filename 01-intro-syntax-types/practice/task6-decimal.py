# Task 6: money to the cent with Decimal
# Run: python 01-intro-syntax-types/practice/task6-decimal.py
#
# 1. The yearly interest of three loans, as Decimal values rounded to cents
#    the SAS / SQL way (ROUND_HALF_UP):  outstanding * rate / 100
#    interest1, interest2, interest3, and their sum total_interest.
#    Make the Decimal values from the texts (not from floats).
# 2. A fee of 0.125 EUR, rounded to cents in three ways:
#      fee_half_up    Decimal, ROUND_HALF_UP     -> Decimal("0.13")
#      fee_half_even  Decimal, ROUND_HALF_EVEN   -> Decimal("0.12")
#      fee_round      float, with round(..., 2)  -> 0.12 (the same as half even)

import sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

outstanding1, rate1 = "1044231.30", "8.83"
outstanding2, rate2 = "651927.30", "5.44"
outstanding3, rate3 = "644.25", "4.79"
CENT = Decimal("0.01")
fee = "0.125"

# ---- your code ----
interest1 = None
interest2 = None
interest3 = None
total_interest = None

fee_half_up = None
fee_half_even = None
fee_round = None
# ---- end of your code ----

check("interest1", interest1, Decimal("92205.62"))
check("interest2", interest2, Decimal("35464.85"))
check("interest3", interest3, Decimal("30.86"))
check("total_interest", total_interest, Decimal("127701.33"))
check("fee_half_up", fee_half_up, Decimal("0.13"))
check("fee_half_even", fee_half_even, Decimal("0.12"))
check("fee_round", fee_round, 0.12)
