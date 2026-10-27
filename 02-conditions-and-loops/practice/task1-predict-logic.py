# Task 1: predict comparisons and logical expressions
# Run: python 02-conditions-and-loops/practice/task1-predict-logic.py
#
# Each check below compares an expression with your prediction. Do NOT run the
# file first: replace each "?" with the value you expect, then run it.
#
# Remember: and / or return one of their operands - not always True or False.
# Write the prediction in the right type: True and "True" are different answers.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

check('"9" < "1000"', "9" < "1000", "?")
check("9 < 1000", 9 < 1000, "?")
check('"3" == 3', "3" == 3, "?")
check('"2026-09-30" > "2026-10-01"', "2026-09-30" > "2026-10-01", "?")
check("30 < 45 <= 90", 30 < 45 <= 90, "?")
check('"age" in "mortgage"', "age" in "mortgage", "?")
check('"EUR" in ("EUR", "USD")', "EUR" in ("EUR", "USD"), "?")
check('0 or "n/a"', 0 or "n/a", "?")
check('"" or None', "" or None, "?")
check("5 and 0", 5 and 0, "?")
check('not ""', not "", "?")
check("True or 1 / 0", True or 1 / 0, "?")
check('"late" if 0 else "current"', "late" if 0 else "current", "?")
check("None is None", None is None, "?")
