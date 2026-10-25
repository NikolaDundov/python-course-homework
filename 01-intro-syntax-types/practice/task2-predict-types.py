# Task 2: predict the value and the type
# Run: python 01-intro-syntax-types/practice/task2-predict-types.py
#
# Each check below compares an expression with your prediction. Do NOT run the
# file first: replace each "?" with the value you expect, then run it.
#
# Write the prediction in the right type: 3, 3.0 and "3" are three different
# answers. True, False and None without quotes; texts in quotes.
#
# Example: check("1 + 1", 1 + 1, 2)

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

check("7 / 2", 7 / 2, "?")
check("7 // 2", 7 // 2, "?")
check("7 % 2", 7 % 2, "?")
check("6 / 3", 6 / 3, "?")
check("2 ** 10", 2 ** 10, "?")
check("-7 // 2", -7 // 2, "?")
check("1 + 2.0", 1 + 2.0, "?")
check('"5" + "5"', "5" + "5", "?")
check('"-" * 3', "-" * 3, "?")
check("True + True", True + True, "?")
check("int(3.99)", int(3.99), "?")
check("round(2.5)", round(2.5), "?")
check('bool("False")', bool("False"), "?")
check("0.1 + 0.2 == 0.3", 0.1 + 0.2 == 0.3, "?")
