"""Helper for the practice tasks - you do not need to change or understand it yet.

check("what is checked", actual_value, expected_value) prints one line:
  OK     your code gives the expected value
  FAIL   it does not - the lines under it show what you got and what is expected
  TODO   you have not written the code of this part yet
A line "-- Part N: ... ---" shows where a new part of the task starts. When the
program ends it prints one line per part and "N of M checks passed", and, unless
every check is OK, exits with code 1.

A check passes when the value is equal AND of the same type: 5 and 5.0 are
different here, because the type of a value matters in the tasks. Floats are
compared with a tiny tolerance (0.1 + 0.2 counts as 0.3).

In a predict task (a file with "predict" in its name) the third value is your
prediction: "?" prints TODO, a wrong one prints WRONG - never the real result,
so you can change a prediction and run the file again as often as you like.

DATA is the data/ folder of this repository: open(DATA / "loans.csv").
"""
import atexit
import hashlib
import json
import math
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

WIDTH = 64

# ---- colours: only on a terminal, never when NO_COLOR is set ----------------
_use_colour = not os.environ.get("NO_COLOR") and (
    bool(os.environ.get("FORCE_COLOR")) or sys.stdout.isatty())
if _use_colour and sys.platform == "win32":
    try:                                    # let the Windows console show colours
        import ctypes
        _kernel = ctypes.windll.kernel32
        _handle = _kernel.GetStdHandle(-11)
        _mode = ctypes.c_uint32()
        if _kernel.GetConsoleMode(_handle, ctypes.byref(_mode)):
            _kernel.SetConsoleMode(_handle, _mode.value | 4)
    except Exception:
        pass
_CODES = {"green": (32, 39), "red": (31, 39), "yellow": (33, 39), "bold": (1, 22), "dim": (2, 22)}
_STATUS_COLOUR = {"OK": "green", "FAIL": "red", "WRONG": "red", "TODO": "yellow"}


def _paint(colour, text):
    if not _use_colour:
        return text
    on, off = _CODES[colour]
    return f"\x1b[{on}m{text}\x1b[{off}m"


# ---- comparing and showing values -------------------------------------------
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


# ---- the parts of a task file: headings and "your code" blocks --------------
_HEADING = re.compile(r"^\s*# == (.+?) ==\s*$")
_sources = {}


def _starters():
    """The starter code of every task, as published (made by make-tasks.py)."""
    if "starters" not in _sources:
        try:
            _sources["starters"] = json.loads((ROOT / ".starters.json").read_text(encoding="utf-8"))
        except Exception:
            _sources["starters"] = {}
    return _sources["starters"]


def block_key(lines):
    """A short fingerprint of a "your code" block, without blank and comment lines."""
    code = [line.rstrip() for line in lines if line.strip() and not line.strip().startswith("#")]
    return hashlib.sha1("\n".join(code).encode("utf-8")).hexdigest()[:12]


def parse(text):
    """The headings (line, title) and the "your code" blocks (line, fingerprint) of a file."""
    headings, blocks, block, start = [], [], None, 0
    for number, line in enumerate(text.splitlines(), start=1):
        heading = _HEADING.match(line)
        if heading:
            headings.append((number, heading.group(1)))
        if "# ---- end of your code ----" in line:
            if block is not None:
                blocks.append((start, block_key(block)))
            block = None
        elif "# ---- your code" in line:
            block, start = [], number
        elif block is not None:
            block.append(line)
    return headings, blocks


def _source(file):
    if file not in _sources:
        try:
            text = Path(file).read_text(encoding="utf-8")
        except Exception:
            text = ""
        headings, blocks = parse(text)
        try:
            name = Path(file).resolve().relative_to(ROOT).as_posix()
        except ValueError:
            name = None
        starter = _starters().get(name)
        if starter is None or len(starter) != len(blocks):
            started = [True] * len(blocks)        # unknown: compare every check
        else:
            started = [key != first for (_, key), first in zip(blocks, starter)]
        _sources[file] = headings, [(line, s) for (line, _), s in zip(blocks, started)]
    return _sources[file]


def _caller():
    """The task file and the line of it that runs now (at the top level of the file)."""
    frame = sys._getframe(1)
    found = None
    while frame is not None:
        if frame.f_code.co_name == "<module>" and frame.f_globals.get("__name__") == "__main__":
            found = (frame.f_code.co_filename, frame.f_lineno)
        frame = frame.f_back
    return found


class _Part:
    def __init__(self, title, not_started):
        self.title = title
        self.not_started = not_started
        self.ok = self.bad = self.todo = 0


_parts = {}          # in the order they were first seen
_shown = [None]      # the part whose separator was printed last


def _current_part():
    where = _caller()
    title, not_started, key = None, False, None
    if where:
        file, line = where
        headings, blocks = _source(file)
        above = [h for h in headings if h[0] <= line]
        start = above[-1][0] if above else 0
        after = [h[0] for h in headings if h[0] > start]
        end = after[0] if after else math.inf
        mine = [s for (b, s) in blocks if start <= b < end]
        not_started = bool(mine) and not any(mine)
        title = above[-1][1] if above else None
        key = (file, start)
    part = _parts.get(key)
    if part is None:
        part = _parts[key] = _Part(title, not_started)
    if part is not _shown[0]:
        if part.title:
            head = f"-- {part.title} "
            print("\n" + _paint("bold", head + "-" * max(3, WIDTH - len(head))))
        _shown[0] = part
    return part


def _line(status, label, *more):
    print("  " + _paint(_STATUS_COLOUR[status], status.ljust(5)) + "  " + label)
    for text in more:
        print("         " + text)


# ---- check ------------------------------------------------------------------
_count = {"ok": 0, "bad": 0, "todo": 0}
_predict = [False]


def check(label, actual, expected):
    part = _current_part()
    where = _caller()
    predict = bool(where) and "predict" in Path(where[0]).name
    _predict[0] = _predict[0] or predict
    if part.not_started or (predict and isinstance(expected, str) and expected == "?"):
        _count["todo"] += 1
        part.todo += 1
        _line("TODO", label)
    elif _same(actual, expected):
        _count["ok"] += 1
        part.ok += 1
        _line("OK", label)
    elif predict:
        _count["bad"] += 1
        part.bad += 1
        note = ""
        if type(actual) is not type(expected) and str(actual) == str(expected):
            note = _paint("dim", "   (check the type: 5 and \"5\", True and \"True\" are different)")
        _line("WRONG", label + note)
    else:
        _count["bad"] += 1
        part.bad += 1
        hint = _paint("dim", "   (no value - a missing return?)") if actual is None else ""
        _line("FAIL", label, "got:      " + _show(actual) + hint, "expected: " + _show(expected))


def _summary():
    ok, bad, todo = _count["ok"], _count["bad"], _count["todo"]
    total = ok + bad + todo
    if total == 0:
        return
    words = ("right", "not answered yet") if _predict[0] else ("OK", "not started")
    print("\n" + "=" * WIDTH)
    titled = [p for p in _parts.values() if p.title]
    if titled:
        pad = min(52, max(len(p.title) for p in titled))
        for p in titled:
            n = p.ok + p.bad + p.todo
            if p.bad:
                state = _paint("red", f"{p.ok} of {n} {words[0]}")
            elif p.todo:
                state = _paint("yellow", words[1] if p.ok == 0 else f"{p.ok} of {n} {words[0]}")
            else:
                state = _paint("green", f"all {words[0]}")
            print(p.title.ljust(pad) + "  " + state)
        print()
    if _predict[0]:
        print(f"Right: {ok} of {total}.  Wrong: {bad}.  Not answered yet: {todo}.")
        if bad:
            print("For each WRONG: read the lecture section again and change your prediction.")
            print("Still WRONG after that? Write to the trainer - we will discuss it in class.")
        elif todo:
            print('Replace each "?" with your prediction.')
        else:
            print("All predictions are right.")
    else:
        print(f"{ok} of {total} checks passed.  Failed: {bad}.  Not started: {todo}.")
    sys.stdout.flush()
    if ok < total:
        os._exit(1)


atexit.register(_summary)
