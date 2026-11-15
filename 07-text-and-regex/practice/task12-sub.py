# Task 12 (Self-study): clean and reformat with re.sub
# Run: python 07-text-and-regex/practice/task12-sub.py
#
# Do this task after you read the Self-study topics "More functions of re"
# and "Named groups, back-references, a function as the replacement" of
# lecture 7.

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: white space ==
# squeeze(text)        every run of white space -> one space; no spaces at the
#                      ends (re.sub + strip)

# ---- your code: part 1 ----
def squeeze(text):
    return text
# ---- end of your code ----

check("squeeze", squeeze("  Iron \t  Retail\nET  "), "Iron Retail ET")

# =============================================================================
# == Part 2: digits only ==
# digits_only(text)    remove everything that is not a digit

# ---- your code: part 2 ----
def digits_only(text):
    return text
# ---- end of your code ----

check("digits_only", digits_only("BG 131-234 567"), "131234567")

# =============================================================================
# == Part 3: ISO dates ==
# iso_dates(text)      every date dd.mm.yyyy in the text -> yyyy-mm-dd
#                      (back-references), the rest unchanged

# ---- your code: part 3 ----
def iso_dates(text):
    return text
# ---- end of your code ----

check("iso_dates", iso_dates("paid on 15.09.2026, review 01.03.2027, ref 1.2.3"),
      "paid on 2026-09-15, review 2027-03-01, ref 1.2.3")

# =============================================================================
# == Part 4: mask an IBAN ==
# mask_iban(text)      every IBAN BG... of 22 characters (no spaces) in the
#                      text: keep the first 8 characters, replace the other
#                      14 with "*"

# ---- your code: part 4 ----
def mask_iban(text):
    return text
# ---- end of your code ----

check("mask_iban", mask_iban("to IBAN BG46FAKE96787581635390 confirmed"), "to IBAN BG46FAKE************** confirmed")

# =============================================================================
# == Part 5: a function as the replacement ==
# bg_to_en_amounts(text)  every amount like "2 069,77" -> "2069.77" (a function
#                      as the replacement); the rest unchanged

# ---- your code: part 5 ----
def bg_to_en_amounts(text):
    return text
# ---- end of your code ----

check("bg_to_en_amounts", bg_to_en_amounts("Payment of 2 069,77 EUR and 45 544,40 EUR"),
      "Payment of 2069.77 EUR and 45544.40 EUR")

# =============================================================================
# == Part 6: count the replacements ==
# count_fixes(texts, pattern, replacement)  a tuple (new_texts, total number of
#                      replacements in all texts) - use re.subn

# ---- your code: part 6 ----
def count_fixes(texts, pattern, replacement):
    return None
# ---- end of your code ----

check("count_fixes", count_fixes(["a  b", "c   d  e", "f"], r"\s{2,}", " "), (["a b", "c d e", "f"], 3))
