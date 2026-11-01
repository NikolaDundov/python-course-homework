"""Checks for the notebooks (NN-topic/notebook.ipynb) - you do not need to change or
understand it yet.

check("what is checked", actual_value, expected_value) prints one line:
  OK     your code gives the expected value
  FAIL   it does not - the lines under it show what you got and what is expected
  TODO   the value is still None: you have not written the code of this part yet
summary() prints how many checks are OK - the last cell of every notebook runs it.

The values are compared as in check.py (the .py tasks): equal AND of the same type,
so 5 and 5.0 are different. Floats are compared with a tiny tolerance.

If you run a check cell again, its new result replaces the old one in the summary.
"""
import os

from check import _same, _show

_CODES = {"OK": 32, "FAIL": 31, "TODO": 33}
_results = {}          # label -> "OK" / "FAIL" / "TODO", in the order first seen


def _paint(status):
    if os.environ.get("NO_COLOR"):
        return status.ljust(5)
    return f"\x1b[{_CODES[status]}m{status.ljust(5)}\x1b[39m"


def check(label, actual, expected):
    if actual is None and expected is not None:
        status, more = "TODO", []
    elif _same(actual, expected):
        status, more = "OK", []
    else:
        status = "FAIL"
        more = ["got:      " + _show(actual), "expected: " + _show(expected)]
    _results[label] = status
    print("  " + _paint(status) + "  " + label)
    for text in more:
        print("         " + text)


def summary():
    statuses = list(_results.values())
    ok, bad, todo = (statuses.count(s) for s in ("OK", "FAIL", "TODO"))
    total = len(statuses)
    if total == 0:
        print("No checks have run yet: run the cells from the top (Run All).")
        return
    print(f"{ok} of {total} checks OK.  Failed: {bad}.  Not done yet: {todo}.")
    failed = [label for label, s in _results.items() if s != "OK"]
    if failed:
        print("Not OK yet: " + ", ".join(failed))
    else:
        print("All checks are OK. Last step: Restart the kernel and Run All - still all OK?")
