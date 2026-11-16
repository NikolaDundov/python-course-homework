# Task 3: split and join
# Run: python 07-text-and-regex/practice/task3-split-join.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: parse settings ==
# parse_settings(text)    "lgd=0.45;currency=EUR" -> {"lgd": "0.45", "currency": "EUR"}
#     Spaces around keys and values are removed; empty parts (";;" or a ";"
#     at the end) are skipped.

# ---- your code: part 1 ----
def parse_settings(text):
    return {}
# ---- end of your code ----

check('parse_settings("lgd=0.45;currency=EUR")', parse_settings("lgd=0.45;currency=EUR"),
      {"lgd": "0.45", "currency": "EUR"})
check('parse_settings(" lgd = 0.45 ;; report_date=2026-09-30;")',
      parse_settings(" lgd = 0.45 ;; report_date=2026-09-30;"), {"lgd": "0.45", "report_date": "2026-09-30"})

# =============================================================================
# == Part 2: settings as text ==
# settings_text(settings) the reverse: a dict -> "key=value;key=value", the keys
#     in alphabetical order

# ---- your code: part 2 ----
def settings_text(settings):
    return ""
# ---- end of your code ----

check('settings_text({"lgd": "0.45", "currency": "EUR"})', settings_text({"lgd": "0.45", "currency": "EUR"}),
      "currency=EUR;lgd=0.45")

# =============================================================================
# == Part 3: SAS SCAN ==
# scan(text, n, sep)      like SAS SCAN: the n-th field (from 1) of text split
#     by sep; a negative n counts from the end (-1 is the last field); ""
#     if there is no such field (also when n is 0)

# ---- your code: part 3 ----
def scan(text, n, sep):
    return ""
# ---- end of your code ----

check('scan("L000002,C0132,investment", 2, ",")', scan("L000002,C0132,investment", 2, ","), "C0132")
check('scan("L000002,C0132,investment", -1, ",")', scan("L000002,C0132,investment", -1, ","), "investment")
check('scan("a b", 5, " ")', scan("a b", 5, " "), "")

# =============================================================================
# == Part 4: a CSV line ==
# to_csv_line(values)     a list of values of any type -> one CSV line with ","
#     between them; None becomes an empty field; a float is written with
#     2 decimals (type(v) == float is True for a float); every other value
#     as str(v)

# ---- your code: part 4 ----
def to_csv_line(values):
    return ""
# ---- end of your code ----

check('to_csv_line(["L000002", 651927.3, 2, None, "EUR"])', to_csv_line(["L000002", 651927.3, 2, None, "EUR"]),
      "L000002,651927.30,2,,EUR")

# =============================================================================
# == Part 5: the legal form of a company ==
# legal_form(name)        the last word of a company name, if it is one of
#     OOD, EOOD, AD, EAD, ET (any case, points removed: "e.o.o.d." -> "EOOD");
#     else ""
LEGAL_FORMS = ("OOD", "EOOD", "AD", "EAD", "ET")

# ---- your code: part 5 ----
def legal_form(name):
    return ""
# ---- end of your code ----

check('legal_form("Black Sea Design ET")', legal_form("Black Sea Design ET"), "ET")
check('legal_form("Green Build e.a.d.")', legal_form("Green Build e.a.d."), "EAD")
check('legal_form("Nikolay Kolev")', legal_form("Nikolay Kolev"), "")
check('legal_form("")', legal_form(""), "")

# =============================================================================
# == Part 6: the words of a comment ==
# words_of(comment)       the words of a comment, in lower case, without the
#     punctuation . , ; : at their ends, and without empty words

# ---- your code: part 6 ----
def words_of(comment):
    return []
# ---- end of your code ----

check('words_of("Overdue 35 days. Reminder sent; call: tomorrow.")',
      words_of("Overdue 35 days. Reminder sent; call: tomorrow."),
      ["overdue", "35", "days", "reminder", "sent", "call", "tomorrow"])
