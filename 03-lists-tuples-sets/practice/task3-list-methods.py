# Task 3: the methods of a list
# Run: python 03-lists-tuples-sets/practice/task3-list-methods.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: change a watch list ==
# watch is a watch list of loans. First make backup: a COPY of watch (not the
# same list!). Then change watch, step by step, with the methods of list:
#   1. add "L000059" at the end
#   2. insert "L000003" at the start (index 0)
#   3. remove "L000025"
#   4. add both "L000077" and "L000103" at the end, with one call
#   5. remove the last loan, and keep it in removed
#   6. sort watch from the largest id to the smallest
# backup must still be the list from the start.
watch = ["L000014", "L000025", "L000012"]
watch_copy = watch.copy()

# ---- your code: part 1 ----
backup = watch.copy()

watch.append("L000059")
watch.insert(0,"L000003")
watch.remove("L000025")
watch.extend(["L000077", "L000103"])

removed = watch.pop()
watch.sort(reverse=True)
print(watch)

# ---- end of your code ----

check("watch", watch, ["L000077", "L000059", "L000014", "L000012", "L000003"])
check("removed", removed, "L000103")
check("backup", backup, ["L000014", "L000025", "L000012"])

# =============================================================================
# == Part 2: size and position ==
#   size        the number of loans in watch
#   position    the index of "L000059" in watch

# ---- your code: part 2 ----
size = len(watch)
position = watch.index("L000059" )
# ---- end of your code ----

check("size", size, 5)
check("position", position, 1)

# =============================================================================
# == Part 3: a sorted copy ==
# names_sorted: the names sorted alphabetically, WITHOUT changing names.
names = ["Maria", "Ivan", "Asen"]

# ---- your code: part 3 ----
names_sorted = sorted(names)
# ---- end of your code ----

check("names_sorted", names_sorted, ["Asen", "Ivan", "Maria"])
check("names", names, ["Maria", "Ivan", "Asen"])
