# Homework 7, optional: read the comments
# Run: python 07-text-and-regex/homework2-comments.py
#
# This homework is optional. It needs only sections 7 - 11 of lecture 7
# (re.search, groups, re.sub) and the dictionaries of lecture 6.

import csv
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the repository root, where check.py is
from check import check, DATA

# rows: the rows of data/loan_comments.csv (dicts with the columns loan_id,
# comment_date, comment).
with open(DATA / "loan_comments.csv", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

# =============================================================================
# == Part 1: the type of a comment ==
# comment_type(text)    the type of a comment, by the FIRST of these rules
#                       that matches (use re.search / re.match):
#                         "payment"        starts with "Payment of"
#                         "restructuring"  contains "restructuring"
#                         "collateral"     starts with "Collateral revalued"
#                         "reminder"       starts with "Overdue", a number, " days"
#                         "refinancing"    starts with "Refinanced from loan L" + 6 digits
#                         "disbursement"   starts with "Disbursement to IBAN"
#                         "guarantee"      contains "EIK " and 9 or 13 digits
#                         "rate change"    starts with "Rate changed"
#                         "review"         starts with "Annual review"
#                       and "other" if none matches

# ---- your code: part 1 ----
def comment_type(text):
    return None
# ---- end of your code ----

check('comment_type("Payment of 1 250,00 EUR received on 15.09.2026.")',
      comment_type("Payment of 1 250,00 EUR received on 15.09.2026."), "payment")
check('comment_type("Guarantee from the parent company, EIK 274692063.")',
      comment_type("Guarantee from the parent company, EIK 274692063."), "guarantee")
check('comment_type("Phone call.")', comment_type("Phone call."), "other")

# =============================================================================
# == Part 2: count the types ==
# type_counts(rows)     a dict type -> number of comments (only the types that
#                       occur)

# ---- your code: part 2 ----
def type_counts(rows):
    return {}
# ---- end of your code ----

check("type_counts(rows)", type_counts(rows), {'review': 56, 'collateral': 30, 'refinancing': 29, 'rate change': 17, 'reminder': 28, 'guarantee': 7, 'disbursement': 21, 'restructuring': 19, 'payment': 24})

# =============================================================================
# == Part 3: the payments ==
# payments(rows)        a list of tuples (loan_id, date, amount) of the
#                       payment comments: date a datetime.date from the
#                       "received on dd.mm.yyyy" part, amount a float from
#                       "Payment of 2 069,77 EUR"; in the order of the file

# ---- your code: part 3 ----
def payments(rows):
    return []
# ---- end of your code ----

pays = payments(rows)
check("len(payments(rows))", len(pays), 24)
check("payments(rows)[:2]", pays[:2], [('L000274', date(2026, 4, 26), 2069.77), ('L000384', date(2026, 4, 26), 6526.65)])
check("the total of the payments", round(sum(p[2] for p in pays), 2), 507043.93)

# =============================================================================
# == Part 4: the new maturities ==
# new_maturities(rows)  a dict loan_id -> the new maturity (a datetime.date)
#                       of the restructuring comments ("new maturity
#                       yyyy-mm-dd"); if a loan has several, the latest date

# ---- your code: part 4 ----
def new_maturities(rows):
    return {}
# ---- end of your code ----

mats = new_maturities(rows)
check("len(new_maturities(rows))", len(mats), 19)
check("the latest new maturity", max(mats.values()) if mats else None, date(2040, 6, 27))

# =============================================================================
# == Part 5: the disbursement IBANs ==
# disbursement_ibans(rows)  a dict loan_id -> the IBAN of the disbursement
#                       comment, without spaces

# ---- your code: part 5 ----
def disbursement_ibans(rows):
    return {}
# ---- end of your code ----

ibans = disbursement_ibans(rows)
check("len(disbursement_ibans(rows))", len(ibans), 20)
check("all IBANs have 22 characters", all(len(x) == 22 for x in ibans.values()) if ibans else None, True)

# =============================================================================
# == Part 6: IBANs that do not match the register ==
# iban_mismatches(ibans, loans, register_rows)
#     ibans is the dict of part 5; loans and register_rows are the rows of
#     data/loans.csv and data/client_register.csv (read below, as given code).
#     Return the loan_ids (sorted) whose disbursement IBAN differs from the
#     IBAN of the loan's client in the register. Clean the client ids of the
#     register (keep the digits, "C" + 4 digits) and the IBANs (no spaces,
#     upper case).
with open(DATA / "loans.csv", encoding="utf-8") as file:
    loans = list(csv.DictReader(file))
with open(DATA / "client_register.csv", encoding="utf-8") as file:
    register_rows = list(csv.DictReader(file))

# ---- your code: part 6 ----
def iban_mismatches(ibans, loans, register_rows):
    return None
# ---- end of your code ----

check("iban_mismatches(...)", iban_mismatches(ibans, loans, register_rows), [])
check("iban_mismatches with a changed IBAN",
      iban_mismatches({"L000151": "BG00FAKE00000000000000"}, loans, register_rows),
      ["L000151"])
