# Task 6: write patterns
# Run: python 07-text-and-regex/practice/task6-first-patterns.py
#
# Give each name a PATTERN (a raw string r"..."). The checks use them with
# re.fullmatch (the whole text must fit) or re.findall (all matches in a text).

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check


def full(pattern, texts):
    """For the checks: does each text fit the pattern (re.fullmatch)?"""
    return [bool(re.fullmatch(pattern, t)) for t in texts] if pattern else None


# =============================================================================
# == Part 1: a loan id ==
# LOAN_ID     "L" and exactly 6 digits                       (fullmatch)

# ---- your code: part 1 ----
LOAN_ID = r""
# ---- end of your code ----

check("LOAN_ID", full(LOAN_ID, ["L000001", "L00001", "l000001", "L0000012", "LA00001"]),
      [True, False, False, False, False])

# =============================================================================
# == Part 2: a client id ==
# CLIENT_ID   "C" and exactly 4 digits                       (fullmatch)

# ---- your code: part 2 ----
CLIENT_ID = r""
# ---- end of your code ----

check("CLIENT_ID", full(CLIENT_ID, ["C0001", "C001", "c0001", "C00010"]), [True, False, False, False])

# =============================================================================
# == Part 3: a currency ==
# CURRENCY    exactly 3 capital Latin letters                (fullmatch)

# ---- your code: part 3 ----
CURRENCY = r""
# ---- end of your code ----

check("CURRENCY", full(CURRENCY, ["EUR", "eur", "EU", "EURO", "BG1"]), [True, False, False, False, False])

# =============================================================================
# == Part 4: a product code ==
# PRODUCT     lower-case Latin letters and "_" only, at least 2 characters
#             ("credit_card", "mortgage")                    (fullmatch)

# ---- your code: part 4 ----
PRODUCT = r""
# ---- end of your code ----

check("PRODUCT", full(PRODUCT, ["credit_card", "mortgage", "Mortgage", "x", "credit card", "loan2"]),
      [True, True, False, False, False, False])

# =============================================================================
# == Part 5: a year ==
# YEAR        a whole word of 4 digits that starts with 19 or 20   (findall)

# ---- your code: part 5 ----
YEAR = r""
# ---- end of your code ----

check("YEAR", re.findall(YEAR, "from 1998 to 2026, ref 12026, 2104 and 2030") if YEAR else None,
      ["1998", "2026", "2030"])

# =============================================================================
# == Part 6: a percent ==
# PERCENT     a number with an optional decimal part (a point and digits),
#             followed by "%" - the % is part of the match   (findall)

# ---- your code: part 6 ----
PERCENT = r""
# ---- end of your code ----

check("PERCENT", re.findall(PERCENT, "rates 12.97% and 13% (was 4.5 %), fee 2.5") if PERCENT else None,
      ["12.97%", "13%"])

# =============================================================================
# == Part 7: a whole word ==
# WORD_EUR    the word "EUR" in any case, as a whole word: not in "EURO"
#             (findall with re.IGNORECASE)

# ---- your code: part 7 ----
WORD_EUR = r""
# ---- end of your code ----

check("WORD_EUR", re.findall(WORD_EUR, "100 EUR, 50 eur, 20 Euro, EURO 5, (Eur)", flags=re.I) if WORD_EUR else None,
      ["EUR", "eur", "Eur"])
