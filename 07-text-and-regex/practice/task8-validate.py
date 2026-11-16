# Task 8: validators with fullmatch
# Run: python 07-text-and-regex/practice/task8-validate.py
#
# Write each function with a regular expression and re.fullmatch. Each returns
# True or False.

import calendar
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: a loan id ==
# is_loan_id(s)     "L" and 6 digits

# ---- your code: part 1 ----
def is_loan_id(s):
    return None
# ---- end of your code ----

check("is_loan_id", [is_loan_id(s) for s in ["L000001", "L00001", "L000001 "]], [True, False, False])

# =============================================================================
# == Part 2: an EIK ==
# is_eik(s)         9 digits or 13 digits (only the shape)

# ---- your code: part 2 ----
def is_eik(s):
    return None
# ---- end of your code ----

check("is_eik", [is_eik(s) for s in ["175591301", "1965730713386", "12345678901", "17559130X"]],
      [True, True, False, False])

# =============================================================================
# == Part 3: a Bulgarian IBAN ==
# is_iban_bg(s)     BG, 2 digits, 4 capital letters, 6 digits, 8 capital
#                   letters or digits - 22 characters, no spaces

# ---- your code: part 3 ----
def is_iban_bg(s):
    return None
# ---- end of your code ----

check("is_iban_bg", [is_iban_bg(s) for s in ["BG05TEST77018249464461", "bg05test77018249464461",
                                               "BG05 TEST 7701 8249 4644 61", "BG05TEST7701824946446"]],
      [True, False, False, False])

# =============================================================================
# == Part 4: an e-mail ==
# is_email(s)       something without "@" and spaces, "@", something without
#                   "@" and spaces, ".", 2 or more letters

# ---- your code: part 4 ----
def is_email(s):
    return None
# ---- end of your code ----

check("is_email", [is_email(s) for s in ["yana.koleva@example.org", "a@b", "a b@example.com",
                                           "x@@example.com", "office@example.c"]],
      [True, False, False, False, False])

# =============================================================================
# == Part 5: a real date ==
# is_date_bg(s)     dd.mm.yyyy with a REAL date: the shape with a regex, then
#                   1 <= month <= 12 and the day in the month (use the
#                   calendar module: calendar.monthrange(year, month)[1] is
#                   the number of days of a month)

# ---- your code: part 5 ----
def is_date_bg(s):
    return None
# ---- end of your code ----

check("is_date_bg", [is_date_bg(s) for s in ["30.09.2026", "31.09.2026", "29.02.2028", "29.02.2026",
                                               "2026-09-30", "30.9.2026"]],
      [True, False, True, False, False, False])

# =============================================================================
# == Part 6: the bad values of a column ==
# bad_values(values, validator)   a function: the values for which the
#                   validator says False, in their order

# ---- your code: part 6 ----
def bad_values(values, validator):
    return None
# ---- end of your code ----

check("bad_values(ids, is_loan_id)", bad_values(["L000001", "X1", "L000002", "L1"], is_loan_id), ["X1", "L1"])
