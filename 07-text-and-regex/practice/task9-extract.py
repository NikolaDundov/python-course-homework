# Task 9 (optional): extract values from free text
# Run: python 08-regular-expressions/practice/task4-extract.py

import csv
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check, DATA

# =============================================================================
# == Part 1: loan ids ==
# loan_ids(text)       all loan ids (L + 6 digits, whole words), in order

# ---- your code: part 1 ----
def loan_ids(text):
    return []
# ---- end of your code ----

check("loan_ids", loan_ids("from loan L000391; L000048, XL0000011 and L000387."), ["L000391", "L000048", "L000387"])

# =============================================================================
# == Part 2: dates ==
# dates(text)          all dates written as dd.mm.yyyy in the text, as
#                      datetime.date objects, in their order in the text.
#                      Dates in other formats are skipped. Hint: a pattern with
#                      three groups; re.findall then gives a list of tuples
#                      (day, month, year) of strings.

# ---- your code: part 2 ----
def dates(text):
    return []
# ---- end of your code ----

check("dates", dates("on 15.09.2026, 22/09/2026 and 01.03.2027; not 2026-04-24"),
      [date(2026, 9, 15), date(2027, 3, 1)])

# =============================================================================
# == Part 3: amounts in EUR ==
# amounts_eur(text)    all amounts followed by " EUR", as floats. The amounts
#                      look like "2 069,77" (Bulgarian) or "20,960.03" /
#                      "99,400" (English, thousands with a comma). Rule: if the
#                      text ends with "," and 2 digits, the comma is the decimal
#                      separator; otherwise commas and spaces are thousands
#                      separators.

# ---- your code: part 3 ----
def amounts_eur(text):
    return []
# ---- end of your code ----

check("amounts_eur (Bulgarian)", amounts_eur("Payment of 2 069,77 EUR received; 45 544,40 EUR"), [2069.77, 45544.4])
check("amounts_eur (English)", amounts_eur("old balance 20,960.03 EUR; valued 99,400 EUR; 5 USD"), [20960.03, 99400.0])

# =============================================================================
# == Part 4: percents ==
# percents(text)       all numbers followed by "%", as floats

# ---- your code: part 4 ----
def percents(text):
    return []
# ---- end of your code ----

check("percents", percents("Rate changed from 12.97% to 13% as of 22.03.2026."), [12.97, 13.0])

# =============================================================================
# == Part 5: statistics of the comments file ==
# comment_stats(rows)  rows are the rows of loan_comments.csv (read below, as
#                      given code: a list of dicts); the text is in the
#                      column "comment". Return a tuple of three values:
#                        1. how many comments have at least one date
#                           dd.mm.yyyy in their text (use dates of part 2);
#                        2. the sum of all EUR amounts in all comments,
#                           rounded to 2 decimals (use amounts_eur of part 3);
#                        3. how many DIFFERENT loan ids are mentioned in the
#                           texts of the comments (use loan_ids of part 1;
#                           the column loan_id of the file does not count).
with open(DATA / "loan_comments.csv", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

# ---- your code: part 5 ----
def comment_stats(rows):
    return None
# ---- end of your code ----

check("comment_stats(rows)", comment_stats(rows), (127, 8087160.77, 28))
