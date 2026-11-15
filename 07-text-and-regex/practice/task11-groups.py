# Task 11 (Self-study): named groups
# Run: python 07-text-and-regex/practice/task11-groups.py
#
# Do this task after you read the Self-study topic "Named groups,
# back-references, a function as the replacement" of lecture 7.

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: a payment line ==
# parse_payment(line)   a line like "P00017,L000034,2026-09-12,1250.00,EUR"
#     -> a dict {"payment_id": ..., "loan_id": ..., "date": ..., "amount": ...,
#     "currency": ...} with the TEXT of each field, made with ONE pattern with
#     named groups and groupdict(). The amount may be negative and may have
#     decimals. None if the line does not fit the pattern.

# ---- your code: part 1 ----
def parse_payment(line):
    return None
# ---- end of your code ----

check("parse_payment(good)", parse_payment("P00017,L000034,2026-09-12,1250.00,EUR"),
      {"payment_id": "P00017", "loan_id": "L000034", "date": "2026-09-12", "amount": "1250.00", "currency": "EUR"})
check("parse_payment(negative)", (parse_payment("P00096,L000201,2026-09-03,-75,USD") or {}).get("amount"), "-75")
check("parse_payment(bad amount)", parse_payment("P00033,L000070,2026-09-05,12O.50,EUR"), None)
check("parse_payment(missing field)", parse_payment("P00120,L000070,2026-09-05,100.00"), None)

# =============================================================================
# == Part 2: a file name ==
# parse_file_name(name) "loans_2026-09.csv" or "payments_2026-09.xlsx" ->
#     a tuple (kind, year, month, extension): ("loans", 2026, 9, "csv");
#     year and month as int. None if the name does not fit.

# ---- your code: part 2 ----
def parse_file_name(name):
    return None
# ---- end of your code ----

check('parse_file_name("loans_2026-09.csv")', parse_file_name("loans_2026-09.csv"), ("loans", 2026, 9, "csv"))
check('parse_file_name("fx_rates_2026-07.xlsx")', parse_file_name("fx_rates_2026-07.xlsx"), ("fx_rates", 2026, 7, "xlsx"))
check('parse_file_name("loans.csv")', parse_file_name("loans.csv"), None)

# =============================================================================
# == Part 3: a rate change ==
# rate_change(comment)  "Rate changed from 12.97% to 13.47% as of 22.03.2026."
#     -> a tuple (old, new, date_iso): (12.97, 13.47, "2026-03-22"); None if
#     the comment is not a rate change.

# ---- your code: part 3 ----
def rate_change(comment):
    return None
# ---- end of your code ----

check("rate_change(...)", rate_change("Rate changed from 12.97% to 13.47% as of 22.03.2026."),
      (12.97, 13.47, "2026-03-22"))
check("rate_change(other)", rate_change("Annual review done on 22.03.2026."), None)

# =============================================================================
# == Part 4: a company name and its legal form ==
# split_name(name)      a company name -> a tuple (base, legal_form), where the
#     legal form is one of OOD, EOOD, AD, EAD, ET at the end, any case, with
#     or without points; legal_form in capitals without points, or None.
#     "Green Build E.A.D." -> ("Green Build", "EAD"); "Nikolay Kolev" ->
#     ("Nikolay Kolev", None)

# ---- your code: part 4 ----
def split_name(name):
    return None
# ---- end of your code ----

check('split_name("Green Build E.A.D.")', split_name("Green Build E.A.D."), ("Green Build", "EAD"))
check('split_name("rila print eood")', split_name("rila print eood"), ("rila print", "EOOD"))
check('split_name("Nikolay Kolev")', split_name("Nikolay Kolev"), ("Nikolay Kolev", None))
