"""Helper for the practice tasks - you do not need to change or understand it yet.

check("what is checked", actual_value, expected_value) prints OK or FAIL.
After the last check, the script prints "N of M checks passed" and exits with
code 1 if any check failed.

A check passes when the value is equal AND of the same type: 5 and 5.0 are
different here, because the type of a value matters in the tasks. Floats are
compared with a tiny tolerance (0.1 + 0.2 counts as 0.3).

DATA is the data/ folder of this repository: open(DATA / "loans.csv").
"""
import atexit
import math
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

_total = 0
_passed = 0


def _same(actual, expected):
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, float):
        if math.isnan(expected):
            return math.isnan(actual)
        return math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-12)
    if hasattr(expected, "equals"):          # pandas Series and DataFrame
        return bool(expected.equals(actual))
    if type(expected).__module__ == "numpy" and hasattr(expected, "shape"):
        import numpy
        return bool(numpy.array_equal(actual, expected))
    try:
        return bool(actual == expected)
    except Exception:
        return False


def _show(value):
    return f"{value!r} ({type(value).__name__})"


def check(label, actual, expected):
    global _total, _passed
    _total += 1
    if _same(actual, expected):
        _passed += 1
        print("OK   " + label)
    else:
        print(f"FAIL {label}: got {_show(actual)}, expected {_show(expected)}")


def _summary():
    if _total == 0:
        return
    print(f"{_passed} of {_total} checks passed")
    sys.stdout.flush()
    if _passed < _total:
        os._exit(1)


atexit.register(_summary)
