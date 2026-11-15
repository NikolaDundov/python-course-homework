# Task 10 (Self-study): numbers from text, and back
# Run: python 07-text-and-regex/practice/task10-amounts.py
#
# Do this task after you read the Self-study topics "Numbers in any format"
# and "translate: change or delete characters" of lecture 7.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: the Bulgarian format ==
# parse_bg(raw)        the Bulgarian format: spaces between thousands, a comma
#     for the decimals: "1 234 567,89" -> 1234567.89. None if empty.

# ---- your code: part 1 ----
def parse_bg(raw):
    return None
# ---- end of your code ----

check('parse_bg("1 234 567,89")', parse_bg("1 234 567,89"), 1234567.89)
check('parse_bg("644,25")', parse_bg("644,25"), 644.25)
check('parse_bg("")', parse_bg(""), None)

# =============================================================================
# == Part 2: any format ==
# parse_amount(raw)    any of: "1 234 567,89", "1.234.567,89", "1,234,567.89",
#     "1234567.89", "EUR 7 729 271" (EUR in front, any case). The LAST "," or
#     "." is the decimal separator if 1 or 2 digits follow it; all other "," /
#     "." / spaces are thousands separators. None if empty.

# ---- your code: part 2 ----
def parse_amount(raw):
    return None
# ---- end of your code ----

check('parse_amount("1.234.567,89")', parse_amount("1.234.567,89"), 1234567.89)
check('parse_amount("1,234,567.89")', parse_amount("1,234,567.89"), 1234567.89)
check('parse_amount("1234567.89")', parse_amount("1234567.89"), 1234567.89)
check('parse_amount("EUR 7 729 271")', parse_amount("EUR 7 729 271"), 7729271.0)
check('parse_amount("eur 12,5")', parse_amount("eur 12,5"), 12.5)
check('parse_amount("  ")', parse_amount("  "), None)

# =============================================================================
# == Part 3: a number in the Bulgarian format ==
# format_bg(value, decimals=2)  a number -> the Bulgarian format, e.g.
#     1234567.891 -> "1 234 567,89"; -5000 with decimals=0 -> "-5 000"

# ---- your code: part 3 ----
def format_bg(value, decimals=2):
    return ""
# ---- end of your code ----

check("format_bg(1234567.891)", format_bg(1234567.891), "1 234 567,89")
check("format_bg(-5000, 0)", format_bg(-5000, 0), "-5 000")
check("format_bg(0.5)", format_bg(0.5), "0,50")

# =============================================================================
# == Part 4: a percent in the Bulgarian format ==
# percent_bg(share)    a share -> a percent with 1 decimal and a comma:
#     0.4736 -> "47,4%"

# ---- your code: part 4 ----
def percent_bg(share):
    return ""
# ---- end of your code ----

check("percent_bg(0.4736)", percent_bg(0.4736), "47,4%")

# =============================================================================
# == Part 5: a total of texts ==
# total_bg(texts)      the sum of a list of amounts in any format (empty ones
#     are skipped), returned in the Bulgarian format with 2 decimals

# ---- your code: part 5 ----
def total_bg(texts):
    return ""
# ---- end of your code ----

check('total_bg(["1 000,50", "", "2,000.25", "EUR 3 000"])', total_bg(["1 000,50", "", "2,000.25", "EUR 3 000"]),
      "6 000,75")
