# Task 4: from text to values
# Run: python 01-intro-syntax-types/practice/task4-convert-text.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# == Part 1: convert the fields ==
# The fields of one loan, as they come from a file: every value is a string.
# The outstanding amount was exported in the Bulgarian format.
# Convert each field into a value of the right type:
#   loan_id        str, without the spaces around it     "L000014"
#   amount         float
#   outstanding    float                                 14286.75
#   rate           float
#   days_past_due  int
#   stage          int
#   restructured   bool - True only when the text is "True"
#                  (careful: bool("False") is True)
loan_id_text = " L000014 "
amount_text = "16100.00"
outstanding_text = "14 286,75"
rate_text = "5.27"
days_text = "200"
stage_text = "3"
restructured_text = "False"

# ---- your code: part 1 ----
loan_id = loan_id_text.strip()
amount = float(amount_text)
outstanding = float(outstanding_text.replace(",", ".").replace(" ", ""))
rate = float(rate_text)
days_past_due = int(days_text)
stage = int(stage_text)
restructured = restructured_text == True
# ---- end of your code ----

check("loan_id", loan_id, "L000014")
check("amount", amount, 16100.0)
check("outstanding", outstanding, 14286.75)
check("rate", rate, 5.27)
check("days_past_due", days_past_due, 200)
check("stage", stage, 3)
check("restructured", restructured, False)

# == Part 2: the repaid amount ==
# repaid: amount - outstanding, rounded to 2 decimals.

# ---- your code: part 2 ----
repaid = round(amount - outstanding, 2 )
# ---- end of your code ----

check("repaid", repaid, 1813.25)

# == Part 3: non-performing? ==
# is_non_performing: True when days_past_due is more than 90.

# ---- your code: part 3 ----
is_non_performing = days_past_due > 90
# ---- end of your code ----

check("is_non_performing", is_non_performing, True)
