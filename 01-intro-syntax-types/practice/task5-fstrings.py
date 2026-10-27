# Task 5: f-strings
# Run: python 01-intro-syntax-types/practice/task5-fstrings.py
#
# Build each text with an f-string and a format specification. The expected
# text is in the check under each part.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

client_number = 80
loan_id = "L000001"
product = "investment"
outstanding = 1044231.3
pd_value = 0.0049
rate = 8.83
stage = 1

# == Part 1: a client code ==
# client_code: "C" and client_number with 4 digits, zeros in front -> "C0080"

# ---- your code: part 1 ----
client_code = None
# ---- end of your code ----

check("client_code", client_code, "C0080")

# == Part 2: an amount ==
# amount_text: outstanding with a thousands separator and 2 decimals
# -> "1,044,231.30"

# ---- your code: part 2 ----
amount_text = None
# ---- end of your code ----

check("amount_text", amount_text, "1,044,231.30")

# == Part 3: the amount in the Bulgarian format ==
# amount_bg: the same in the Bulgarian format -> "1 044 231,30"

# ---- your code: part 3 ----
amount_bg = None
# ---- end of your code ----

check("amount_bg", amount_bg, "1 044 231,30")

# == Part 4: a PD as a percent ==
# pd_text: pd_value as a percent with 2 decimals -> "0.49%"

# ---- your code: part 4 ----
pd_text = None
# ---- end of your code ----

check("pd_text", pd_text, "0.49%")

# == Part 5: a rate that is already in percent ==
# rate_text: rate (already in percent) with 2 decimals and a "%" -> "8.83%"

# ---- your code: part 5 ----
rate_text = None
# ---- end of your code ----

check("rate_text", rate_text, "8.83%")

# == Part 6: a sentence ==
# sentence: "Loan L000001 (investment): 1,044,231.30 EUR, stage 1"

# ---- your code: part 6 ----
sentence = None
# ---- end of your code ----

check("sentence", sentence, "Loan L000001 (investment): 1,044,231.30 EUR, stage 1")

# == Part 7: two lines of a report ==
# header and line: two lines of a report, 38 characters each: the loan id
# left in 10 characters, the product left in 13, the outstanding amount
# right in 15 (with separator and 2 decimals). The header has the words
# "loan", "product" and "outstanding" in the same widths.

# ---- your code: part 7 ----
header = None
line = None
# ---- end of your code ----

check("header", header, "loan      product          outstanding")
check("line", line, "L000001   investment      1,044,231.30")
