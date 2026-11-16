# Homework 7: clean the client register
# Run: python 07-text-and-regex/homework.py
#
# data/client_register.csv has the 150 clients with messy text fields. Write one
# function per column (parts 1 - 8). Each function takes the raw text (a str)
# and returns the clean value, or None if the text is empty or cannot be
# cleaned. Parts 9 - 11 clean the whole file. Part 12 finds the payments in
# the comments of data/loan_comments.csv with a regular expression. The files
# are read for you (given code): you work on the rows, lists of dicts.

import csv
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the repository root, where check.py is
from check import check, DATA

# =============================================================================
# == Part 1: the client id ==
# clean_id(raw)      "C" + 4 digits ("c 17" -> "C0017"): remove the spaces and
#                    the "-", make the letter a capital, add zeros in front
#                    of the number until it has 4 digits. None if the text
#                    does not start with C (or c), if the rest is not only
#                    digits, or if there are more than 4 digits.

# ---- your code: part 1 ----
def clean_id(raw):
    return None
# ---- end of your code ----

check('clean_id("C-0026")', clean_id("C-0026"), "C0026")

# =============================================================================
# == Part 2: the name ==
# clean_name(raw)    one space between words, no spaces at the ends, no
#                    double quotes ("), every word in Title Case - but a
#                    word that is a legal form (OOD, EOOD, AD, EAD, ET, in
#                    any case, with or without points) becomes the legal
#                    form in capitals without points: "e.a.d." -> "EAD".
#                    None if no word is left.
LEGAL_FORMS = {"OOD", "EOOD", "AD", "EAD", "ET"}

# ---- your code: part 2 ----
def clean_name(raw):
    return None
# ---- end of your code ----

check('clean_name(\'"Silver  Textiles" a.d.\')', clean_name('"Silver  Textiles" a.d.'), "Silver Textiles AD")

# =============================================================================
# == Part 3: the EIK ==
# clean_eik(raw)     remove the spaces and a "BG" in front (any case). The
#                    result must be 9 or 13 digits, else None.

# ---- your code: part 3 ----
def clean_eik(raw):
    return None
# ---- end of your code ----

check('clean_eik("BG 165 960 351")', clean_eik("BG 165 960 351"), "165960351")

# =============================================================================
# == Part 4: the IBAN ==
# clean_iban(raw)    remove the spaces, make the letters capitals. The result
#                    must have 22 characters, start with "BG" and have only
#                    letters and digits, else None.

# ---- your code: part 4 ----
def clean_iban(raw):
    return None
# ---- end of your code ----

check('clean_iban("bg05 test 7701 8249 4644 61")', clean_iban("bg05 test 7701 8249 4644 61"), "BG05TEST77018249464461")

# =============================================================================
# == Part 5: the e-mail ==
# clean_email(raw)   remove the spaces at the ends, make it lower case. The
#                    result must have exactly one "@", at least one character
#                    before it, a "." somewhere after it, and no spaces
#                    inside - else None.

# ---- your code: part 5 ----
def clean_email(raw):
    return None
# ---- end of your code ----

check('clean_email("office.balkanfoods at example.net")', clean_email("office.balkanfoods at example.net"), None)

# =============================================================================
# == Part 6: the city ==
# clean_city(raw)    the English name of the city. In this order: one space
#                    between words and no spaces at the ends; remove a
#                    "gr. " in front; if the name is a key of CITIES_BG,
#                    take its value; Title Case. None if the result is "".
CITIES_BG = {"София": "Sofia", "Пловдив": "Plovdiv", "Варна": "Varna", "Бургас": "Burgas",
             "Русе": "Ruse", "Стара Загора": "Stara Zagora", "Плевен": "Pleven"}

# ---- your code: part 6 ----
def clean_city(raw):
    return None
# ---- end of your code ----

check('clean_city("  gr. Стара Загора")', clean_city("  gr. Стара Загора"), "Stara Zagora")

# =============================================================================
# == Part 7: the date ==
# clean_date(raw)    a datetime.date. The column has five formats; clean the
#                    two most common ones:
#                      "2014-06-08" (ISO)         -> date(2014, 6, 8)
#                      "08.06.2014" (day first)   -> date(2014, 6, 8)
#                    Remove the spaces at the ends first. Check the shape with
#                    re.fullmatch (4 digits - 2 digits - 2 digits, or 2 digits
#                    . 2 digits . 4 digits). Return None for every other text
#                    (also "08/06/2014", "20140608", "8 Jun 2014" and "").

# ---- your code: part 7 ----
def clean_date(raw):
    return None
# ---- end of your code ----

check('clean_date(" 2014-06-08")', clean_date(" 2014-06-08"), date(2014, 6, 8))
check('clean_date("08.06.2014")', clean_date("08.06.2014"), date(2014, 6, 8))
check('clean_date("8 Jun 2014")', clean_date("8 Jun 2014"), None)
check('clean_date("")', clean_date(""), None)

# =============================================================================
# == Part 8: the amount ==
# clean_amount(raw)  a float. The column has several formats; clean only the
#                    Bulgarian one: "6 639 678,04" -> 6639678.04. Its shape:
#                    1 to 3 digits, then any number of groups "a space and 3
#                    digits" (also no group: "644,25"), then a comma and 2
#                    digits. Remove the spaces at the ends first, check the
#                    shape with re.fullmatch, and return None for every other
#                    text (also "1,234,567.89", "EUR 7 729 271" and "").

# ---- your code: part 8 ----
def clean_amount(raw):
    return None
# ---- end of your code ----

check('clean_amount("6 639 678,04")', clean_amount("6 639 678,04"), 6639678.04)
check('clean_amount(" 644,25 ")', clean_amount(" 644,25 "), 644.25)
check('clean_amount("1,234,567.89")', clean_amount("1,234,567.89"), None)
check('clean_amount("")', clean_amount(""), None)

# =============================================================================
# == Part 9: a clean record ==
# rows: the rows of data/client_register.csv, read below as given code. Each
# row is a dict with the keys client_id, name, eik, iban, email, city,
# registered, turnover and the raw texts as values.
#
# clean_record(row)  row is one row of the file (one dict of rows). Return
#                    a NEW dict with the same keys, where every value is
#                    cleaned by the function of its column (parts 1 - 8).
#                    The checks after part 10 test it.
with open(DATA / "client_register.csv", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

# ---- your code: part 9 ----
def clean_record(row):
    return {}
# ---- end of your code ----

# =============================================================================
# == Part 10: the whole register ==
# clean_register(rows)   rows are the rows of the register (read before
#                    part 9). Return a list with the clean record (part 9)
#                    of every row, in the same order.

# ---- your code: part 10 ----
def clean_register(rows):
    return []
# ---- end of your code ----

records = clean_register(rows)

check("len(records)", len(records), 150)
check("records[25:26]", records[25:26], [{
    "client_id": "C0026", "name": "Silver Textiles AD", "eik": "1965730713386", "iban": "BG27TEST65808265754078",
    "email": "office.silvertextiles@example.org", "city": "Varna", "registered": date(2015, 6, 20),
    "turnover": None}])
check("all ids valid and unique", len({r["client_id"] for r in records if r["client_id"]}), 150)
check("the cities agree with clients.csv", sorted({r["city"] for r in records}) if records else None,
      ["Burgas", "Pleven", "Plovdiv", "Ruse", "Sofia", "Stara Zagora", "Varna"])

# =============================================================================
# == Part 11: a summary of the cleaning ==
# summary(rows, records) rows are the raw rows of the file (read before
#     part 9) and records the clean ones, in the same order (made after
#     part 10).
#     Return a dict column name -> a tuple (changed, invalid), with the eight
#     column names as keys:
#       changed = in how many rows the clean value is not None and
#                 str(clean value) is not equal to the raw text;
#       invalid = in how many rows the clean value is None although the raw
#                 text is not empty (not "" after strip()).
#     str() of a date is its ISO text, so "2014-06-08" counts as unchanged and
#     "08.06.2014" as changed. A float never has the same text as the raw
#     amount, so every cleaned amount counts as changed.

# ---- your code: part 11 ----
def summary(rows, records):
    return {}
# ---- end of your code ----

check("summary(rows, records)", summary(rows, records) if records else None, {'client_id': (55, 0), 'name': (55, 0), 'eik': (10, 0), 'iban': (55, 0), 'email': (28, 2), 'city': (89, 0), 'registered': (43, 40), 'turnover': (19, 40)})

# =============================================================================
# == Part 12: the payments in the comments ==
# data/loan_comments.csv has the columns loan_id, comment_date, comment. A
# payment comment looks like this:
#     Payment of 2 069,77 EUR received on 26.04.2026.
#
# comments: the rows of data/loan_comments.csv, read below as given code (a
# list of dicts with the keys loan_id, comment_date, comment).
#
# payments(comments) Return a list of tuples (loan_id, amount, month) for
#                    the payment comments, in the order of the file:
#                      loan_id   the value of the column loan_id (a str);
#                      amount    the amount of the comment as a float
#                                (2069.77);
#                      month     the year and the month of the "received on"
#                                date as text: "2026-04".
#                    Use ONE pattern with groups and re.search on the column
#                    comment. Comments that do not fit the pattern are skipped.
with open(DATA / "loan_comments.csv", encoding="utf-8") as file:
    comments = list(csv.DictReader(file))

# ---- your code: part 12 ----
def payments(comments):
    return []
# ---- end of your code ----

pays = payments(comments)
check("len(payments(comments))", len(pays), 24)
check("payments(comments)[:2]", pays[:2], [("L000274", 2069.77, "2026-04"), ("L000384", 6526.65, "2026-04")])
check("the total of the payments", round(sum(p[1] for p in pays), 2), 507043.93)
