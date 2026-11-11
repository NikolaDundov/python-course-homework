# Task 2: predict - dictionaries
# Run: python 06-dictionaries/practice/task2-predict-dicts.py
#
# Replace each "?" with the value you expect, then run the file. It prints OK,
# WRONG or TODO for each prediction, never the real result: run it as often as
# you like. For a WRONG, read the lecture section again and change your
# prediction. Write the prediction in the right type: {"a": 1} is a dict, ["a"]
# a list.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

check('{"EUR": 1, "USD": 2, "EUR": 3}', {"EUR": 1, "USD": 2, "EUR": 3}, "?")
check('len({"a": 1, "A": 2})', len({"a": 1, "A": 2}), "?")
check('{"a": 1, "b": 2}["b"]', {"a": 1, "b": 2}["b"], "?")
check('{"a": 1}.get("b")', {"a": 1}.get("b"), "?")
check('{"a": 1}.get("b", 0)', {"a": 1}.get("b", 0), "?")
check('"a" in {"a": 1}', "a" in {"a": 1}, "?")
check('1 in {"a": 1}', 1 in {"a": 1}, "?")
check('list({"b": 2, "a": 1})', list({"b": 2, "a": 1}), "?")
check('sorted({"b": 2, "a": 1})', sorted({"b": 2, "a": 1}), "?")

d = {"x": 1}
d["y"] = 2
d["x"] = 5
check("d after d['y'] = 2 and d['x'] = 5", d, "?")

d = {"x": 1, "y": 2}
check('d.pop("z", 0)', d.pop("z", 0), "?")
check('{"x": 1} | {"x": 5, "z": 3}', {"x": 1} | {"x": 5, "z": 3}, "?")
