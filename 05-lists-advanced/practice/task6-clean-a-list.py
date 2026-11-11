# Task 6 (Optional): clean a list of loans step by step, then report on it
# Run: python 05-lists-advanced/practice/task6-clean-a-list.py
#
# The parts work on the same list, one after the other: do them in order.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# records: tuples (loan_id, outstanding), as they came from a system export.
records = [
    ("L000005", 3127.40),
    ("TEST01", 0.0),
    ("L000001", 1044231.30),
    ("L000003", 0.0),
    ("L000002", 651927.30),
    ("L000004", 5875.11),
    ("L000008", 0.0),
]

# =============================================================================
# == Part 1: remove the test record ==
# ids        the loan_ids of records (a comprehension)
# test_pos   the position of "TEST01" in ids (index)
# Then remove the record at that position from records (del).

# ---- your code: part 1 ----
ids = None
test_pos = None
# ---- end of your code ----

check("test_pos", test_pos, 1)
check("len(records)", len(records), 6)

# =============================================================================
# == Part 2: drop the repaid loans ==
# active    the records with outstanding greater than 0, in a new list

# ---- your code: part 2 ----
active = None
# ---- end of your code ----

check("active", active, [("L000005", 3127.40), ("L000001", 1044231.30), ("L000002", 651927.30), ("L000004", 5875.11)])

# =============================================================================
# == Part 3: sort by id ==
# Sort active (the list of Part 2) itself by loan_id: one call of the method
# sort, with key.

# ---- your code: part 3 ----

# ---- end of your code ----

check("the ids of active", [r[0] for r in active or []], ["L000001", "L000002", "L000004", "L000005"])

# =============================================================================
# == Part 4: totals ==
# total       the sum of outstanding of active, rounded to 2 decimals
# big_count   how many active loans have outstanding over 5000
# (generator expressions)

# ---- your code: part 4 ----
total = None
big_count = None
# ---- end of your code ----

check("total", total, 1705161.11)
check("big_count", big_count, 3)

# =============================================================================
# == Part 5: a ranked report ==
# report    one line of text per active loan, from the largest:
#           "1. L000001: 1,044,231.30" - an f-string with {amount:,.2f}
#           (sorted with key and reverse, enumerate with start=1)

# ---- your code: part 5 ----
report = None
# ---- end of your code ----

check("report", report, ["1. L000001: 1,044,231.30", "2. L000002: 651,927.30",
                         "3. L000004: 5,875.11", "4. L000005: 3,127.40"])
