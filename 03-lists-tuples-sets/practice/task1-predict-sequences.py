# Task 1: predict indexes, slices and operations
# Run: python 03-lists-tuples-sets/practice/task1-predict-sequences.py
#
# Each check below compares an expression with your prediction. Replace each "?"
# with the value you expect, then run the file. It prints OK, WRONG or TODO for
# each prediction, never the real result: run it as often as you like. For a
# WRONG, read the lecture section again and change your prediction.
#
# Write the prediction in the right type: [20, 30] is a list, (20, 30) a tuple,
# {1, 3} a set, "09" a string.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

check("[10, 20, 30, 40][1]", [10, 20, 30, 40][1], 20)
check("[10, 20, 30, 40][-1]", [10, 20, 30, 40][-1], 40)
check("[10, 20, 30, 40][1:3]", [10, 20, 30, 40][1:3], [20, 30])
check('"L000123"[1:]', "L000123"[1:], "000123")
check('"2026-09-30"[5:7]', "2026-09-30"[5:7], "09")
check("[1, 2] + [3]", [1, 2] + [3], [1, 2, 3])
check("[0] * 3", [0] * 3, [0,0,0])
check('"USD" in ["EUR", "USD"]', "USD" in ["EUR", "USD"], True)
check("type((99,)).__name__", type((99,)).__name__, "tuple")
check("sorted([3, 1, 2])", sorted([3, 1, 2]), [1,2,3])
check("[3, 1, 2].sort()", [3, 1, 2].sort(), None)
check("list(range(2, 10, 3))", list(range(2, 10, 3)), [2, 5, 8])
check("len({1, 2, 2, 3})", len({1, 2, 2, 3}), 3)
check("{1, 2, 3} - {2}", {1, 2, 3} - {2}, {1, 3})
