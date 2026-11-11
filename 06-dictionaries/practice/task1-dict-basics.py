# Task 1: a product nomenclature - create, read, change
# Run: python 06-dictionaries/practice/task1-dict-basics.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: create a dict ==
# names    a dict: "mortgage" -> "Mortgage loan", "consumer" -> "Consumer loan",
#          "overdraft" -> "Overdraft"

# ---- your code: part 1 ----
names = {}
# ---- end of your code ----

# =============================================================================
# == Part 2: read with [] ==
# overdraft    the name of "overdraft", read from names with []

# ---- your code: part 2 ----
overdraft = None
# ---- end of your code ----

check("overdraft", overdraft, "Overdraft")

# =============================================================================
# == Part 3: read with get ==
# leasing    the name of "leasing", read with get and the default "Other"

# ---- your code: part 3 ----
leasing = None
# ---- end of your code ----

check("leasing", leasing, "Other")

# =============================================================================
# == Part 4: change the dict ==
# Add "credit_card" -> "Credit card" to names, change "mortgage" to
# "Housing loan", and remove "consumer" with pop - keep its value in `removed`
# (the value that pop returns).

# ---- your code: part 4 ----
removed = None
# ---- end of your code ----

check("removed", removed, "Consumer loan")
check("names", names, {"mortgage": "Housing loan", "overdraft": "Overdraft", "credit_card": "Credit card"})

# =============================================================================
# == Part 5: the sorted keys ==
# codes    a list of the keys of names (after part 4), sorted alphabetically

# ---- your code: part 5 ----
codes = None
# ---- end of your code ----

check("codes", codes, ["credit_card", "mortgage", "overdraft"])

# =============================================================================
# == Part 6: is a key there? ==
# has_leasing    True if "leasing" is a key of names, else False (use in)

# ---- your code: part 6 ----
has_leasing = None
# ---- end of your code ----

check("has_leasing", has_leasing, False)

# =============================================================================
# == Part 7: a lookup with a default ==
# name_of(code, nomenclature)   a function. nomenclature is a dict code -> name
#                               (like names). Return the name of the code, or
#                               the text "Unknown: " followed by the code if
#                               the code is not a key of the nomenclature:
#                               name_of("swap", names) -> "Unknown: swap"

# ---- your code: part 7 ----
def name_of(code, nomenclature):
    return None
# ---- end of your code ----

check('name_of("overdraft", names)', name_of("overdraft", names), "Overdraft")
check('name_of("leasing", names)', name_of("leasing", names), "Unknown: leasing")

# =============================================================================
# == Part 8: a dict from two lists ==
# pd_of_grade    a dict grade -> pd, made from the two lists grades and pds with
#                zip: the first grade with the first pd, and so on
grades = ["AAA", "AA", "A", "BBB"]
pds = [0.0003, 0.0008, 0.0018, 0.0043]

# ---- your code: part 8 ----
pd_of_grade = None
# ---- end of your code ----

check("pd_of_grade", pd_of_grade, {"AAA": 0.0003, "AA": 0.0008, "A": 0.0018, "BBB": 0.0043})
