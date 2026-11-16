# Task 7: predict - regular expressions
# Run: python 07-text-and-regex/practice/task7-predict-regex.py
#
# Replace each "?" with the value you expect, then run the file. It prints OK,
# WRONG or TODO for each prediction, never the real result: run it as often as
# you like. For a WRONG, read the lecture section again and change your
# prediction. A list of strings is ["a", "b"]; a list of tuples is
# [("a", "b"), ("c", "d")]; a match that is not found is None; a bool is
# True / False.

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

check('re.findall(r"\\d+", "a1b22c333")', re.findall(r"\d+", "a1b22c333"), "?")
check('re.findall(r"\\d", "a1b22")', re.findall(r"\d", "a1b22"), "?")
check('re.findall(r"\\d{2}", "12345")', re.findall(r"\d{2}", "12345"), "?")
check('re.findall(r"[A-Z]{3}", "EUR usd GBP")', re.findall(r"[A-Z]{3}", "EUR usd GBP"), "?")
check('bool(re.search(r"^L", "XL1"))', bool(re.search(r"^L", "XL1")), "?")
check('bool(re.search(r"L\\d+", "XL123x"))', bool(re.search(r"L\d+", "XL123x")), "?")
check('bool(re.match(r"L\\d+", "L123x"))', bool(re.match(r"L\d+", "L123x")), "?")
check('bool(re.fullmatch(r"L\\d+", "L123x"))', bool(re.fullmatch(r"L\d+", "L123x")), "?")
check('re.search(r"EUR", "100 eur")', re.search(r"EUR", "100 eur"), "?")
check('re.findall(r"a.c", "abc a.c a-c ac")', re.findall(r"a.c", "abc a.c a-c ac"), "?")
check('re.findall(r"a\\.c", "abc a.c")', re.findall(r"a\.c", "abc a.c"), "?")
check('re.findall(r"\\bAD\\b", "AD EAD ADX AD.")', re.findall(r"\bAD\b", "AD EAD ADX AD."), "?")
check('re.findall(r"(\\d+)-(\\d+)", "1-2 33-44")', re.findall(r"(\d+)-(\d+)", "1-2 33-44"), "?")
check('re.findall(r"\\d+ (EUR|USD)", "5 EUR 7 USD 9 BGN")', re.findall(r"\d+ (EUR|USD)", "5 EUR 7 USD 9 BGN"), "?")
check('re.findall(r"\\d+(?:\\.\\d+)?", "1.5 and 2")', re.findall(r"\d+(?:\.\d+)?", "1.5 and 2"), "?")
check('re.sub(r"\\s+", " ", "a   b  c")', re.sub(r"\s+", " ", "a   b  c"), "?")
check('re.sub(r"\\D", "", "C-00 26")', re.sub(r"\D", "", "C-00 26"), "?")

m = re.search(r"(\d{2})\.(\d{4})", "period 09.2026")
check("m.group(2) after re.search(r\"(\\d{2})\\.(\\d{4})\", \"period 09.2026\")", m.group(2), "?")
