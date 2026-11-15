# Task 2: predict - string methods
# Run: python 07-text-and-regex/practice/task2-predict-strings.py
#
# Replace each "?" with the value you expect, then run the file. It prints OK,
# WRONG or TODO for each prediction, never the real result: run it as often as
# you like. For a WRONG, read the lecture section again and change your
# prediction. Write the prediction in the right type: "a" is a str, ["a"] a
# list, 3 an int.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

check('"a,,b".split(",")', "a,,b".split(","), "?")
check('" a  b ".split()', " a  b ".split(), "?")
check('"L000002".find("0")', "L000002".find("0"), "?")
check('"L000002".find("X")', "L000002".find("X"), "?")
check('"L000002".count("0")', "L000002".count("0"), "?")
check('"**12**".strip("*")', "**12**".strip("*"), "?")
check('"-".join(["2026", "09", "30"])', "-".join(["2026", "09", "30"]), "?")
check('"2026-09-30".split("-")[1]', "2026-09-30".split("-")[1], "?")
check('"Black Sea ET".split()[-1]', "Black Sea ET".split()[-1], "?")
check('"lgd=0.45".split("=")', "lgd=0.45".split("="), "?")
check('"12.50".isdigit()', "12.50".isdigit(), "?")
check('"".isdigit()', "".isdigit(), "?")
check('"7".zfill(3)', "7".zfill(3), "?")
check('"BG80 TEST".replace(" ", "").lower()', "BG80 TEST".replace(" ", "").lower(), "?")
check('"gr. Varna".removeprefix("gr. ")', "gr. Varna".removeprefix("gr. "), "?")
check('"Varna".removeprefix("gr. ")', "Varna".removeprefix("gr. "), "?")
check('"blue wines eood".title()', "blue wines eood".title(), "?")
check('"Sofia" < "sofia"', "Sofia" < "sofia", "?")

s = " C0001 "
s.strip()
check("s after s.strip() without =", s, "?")
