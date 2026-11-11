# Task 2 (optional, Advanced): extra dictionary predictions
# Run: python 06-dictionaries/practice/task2-predict-dicts-advanced.py
#
# Read the Advanced blocks on setdefault and inversion first.
# Replace each "?" with your prediction, then run. WRONG does not show the answer.
# This file is optional; the core prediction task has its own checks.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

d = {"x": 1, "y": 2}
check('d.setdefault("x", 99)', d.setdefault("x", 99), "?")
check('{v: k for k, v in {"a": 1, "b": 1}.items()}', {v: k for k, v in {"a": 1, "b": 1}.items()}, "?")
