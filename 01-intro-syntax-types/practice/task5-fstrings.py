# Task 5: f-strings
# Run: python 01-intro-syntax-types/practice/task5-fstrings.py
#
# Build each text with an f-string and a format specification. The expected
# texts are in the checks at the bottom.
#
# 1. client_code: "C" and client_number with 4 digits, zeros in front  -> "C0080"
# 2. amount_text: outstanding with a thousands separator and 2 decimals
#    -> "1,044,231.30"
# 3. amount_bg: the same in the Bulgarian format -> "1 044 231,30"
# 4. pd_text: pd_value as a percent with 2 decimals -> "0.49%"
# 5. rate_text: rate (already in percent) with 2 decimals and a "%" -> "8.83%"
# 6. sentence: "Loan L000001 (investment): 1,044,231.30 EUR, stage 1"
# 7. header and line: two lines of a report, 38 characters each: the loan id
#    left in 10 characters, the product left in 13, the outstanding amount
#    right in 15 (with separator and 2 decimals). The header has the words
#    "loan", "product" and "outstanding" in the same widths.

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

# ---- your code ----
client_code = None
amount_text = None
amount_bg = None
pd_text = None
rate_text = None
sentence = None
header = None
line = None
# ---- end of your code ----

check("client_code", client_code, "C0080")
check("amount_text", amount_text, "1,044,231.30")
check("amount_bg", amount_bg, "1 044 231,30")
check("pd_text", pd_text, "0.49%")
check("rate_text", rate_text, "8.83%")
check("sentence", sentence, "Loan L000001 (investment): 1,044,231.30 EUR, stage 1")
check("header", header, "loan      product          outstanding")
check("line", line, "L000001   investment      1,044,231.30")
