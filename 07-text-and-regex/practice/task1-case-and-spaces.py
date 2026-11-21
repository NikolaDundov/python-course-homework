# Task 1: case and spaces
# Run: python 07-text-and-regex/practice/task1-case-and-spaces.py
#
# Write the functions. Each one takes a string and RETURNS the clean string.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: extra spaces ==
# squeeze(s)    no spaces at the ends, one space between words
#               ("  Iron   Retail  ET " -> "Iron Retail ET")

# ---- your code: part 1 ----
def squeeze(s):
    return " ".join(s.split())
# ---- end of your code ----

check('squeeze("  Iron   Retail  ET ")', squeeze("  Iron   Retail  ET "), "Iron Retail ET")
check('squeeze("\\tC0001 \\n")', squeeze("\tC0001 \n"), "C0001")

# =============================================================================
# == Part 2: capital letters ==
# proper(s)     squeeze, then every word with a capital first letter
#               ("rila   PRINT" -> "Rila Print")

# ---- your code: part 2 ----
def proper(s):
    return squeeze(s).title()
# ---- end of your code ----

check('proper("rila   PRINT")', proper("rila   PRINT"), "Rila Print")

# =============================================================================
# == Part 3: a city name ==
# clean_city(s)    squeeze, remove a "gr. " in front (only at the start),
#                  then proper ("  gr. stara zagora" -> "Stara Zagora")

# ---- your code: part 3 ----
def clean_city(s):
    squeezed = squeeze(s)
    prefixed = squeezed.removeprefix("gr. ")
    return proper(prefixed)
# ---- end of your code ----

check('clean_city("  gr. stara zagora")', clean_city("  gr. stara zagora"), "Stara Zagora")
check('clean_city("RUSE ")', clean_city("RUSE "), "Ruse")
check('clean_city("gr. ruse")', clean_city("gr. ruse"), "Ruse")

# =============================================================================
# == Part 4: a product code ==
# clean_code(s)    product codes: no spaces at the ends, lower case, inner
#                  spaces and dashes become "_" ("Credit Card" -> "credit_card",
#                  " WORKING-CAPITAL " -> "working_capital")

# ---- your code: part 4 ----
def clean_code(s):
    trimmed = s.strip()
    smaller = trimmed.lower()
    return smaller.replace(" ", "_").replace("-", "_")
# ---- end of your code ----

check('clean_code("Credit Card")', clean_code("Credit Card"), "credit_card")
check('clean_code(" WORKING-CAPITAL ")', clean_code(" WORKING-CAPITAL "), "working_capital")

# =============================================================================
# == Part 5: compare two texts ==
# same_text(a, b)  True if a and b are equal when case and extra spaces are
#                  ignored ("SOFIA " and "sofia" -> True)

# ---- your code: part 5 ----
def same_text(a, b):
    return squeeze(a).lower() == squeeze(b).lower()
# ---- end of your code ----

check('same_text("SOFIA ", "sofia")', same_text("SOFIA ", "sofia"), True)
check('same_text("Stara  Zagora", "stara zagora")', same_text("Stara  Zagora", "stara zagora"), True)
check('same_text("Ruse", "Russe")', same_text("Ruse", "Russe"), False)

# =============================================================================
# == Part 6: initials ==
# initials(name)   the first letters of the words, in capitals, with a point
#                  after each: "nikolay kolev" -> "N.K."

# ---- your code: part 6 ----
def initials(name):
    arr = name.split()
    result = []
    for n in arr:
        result.append(n[0].upper() + ".") 
    return "".join(result)
# ---- end of your code ----

check('initials("nikolay kolev")', initials("nikolay kolev"), "N.K.")
check('initials("  Yana  Petrova Koleva")', initials("  Yana  Petrova Koleva"), "Y.P.K.")
