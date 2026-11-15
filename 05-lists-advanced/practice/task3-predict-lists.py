# Task 3: predict - list methods, comprehensions, generators, zip
# Run: python 05-lists-advanced/practice/task3-predict-lists.py
#
# Replace each "?" with the value you expect, then run the file. It prints OK,
# WRONG or TODO for each prediction, never the real result: run it as often as
# you like. For a WRONG, read the lecture section again and change your
# prediction. Write the prediction in the right type: [1, 2] is a list, (1, 2) a
# tuple, None is None.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: list methods ==
stages = [2, 1, 3, 1]
result = stages.sort()
check("result", result, None)
check("stages", stages, [1, 1, 2, 3])

products = ["overdraft", "mortgage", "overdraft"]
products.remove("overdraft")
check("products", products, ["mortgage", "overdraft"])
check('products.index("overdraft")', products.index("overdraft"), 1)

ids = ["L1", "L2", "L3"]
item = ids.pop(0)
check("item", item, "L1")
check("ids", ids, ["L2", "L3"])
check('sorted(["b", "A", "a"])', sorted(["b", "A", "a"]), ["A", "a", "b"])
check("sorted([3, 1, 2], reverse=True)[:2]", sorted([3, 1, 2], reverse=True)[:2], [3,2])

# =============================================================================
# == Part 2: comprehensions ==
days = [0, 35, 0, 120, 15]
check("[d for d in days if d > 30]", [d for d in days if d > 30], [35, 120])
check("[d if d > 30 else 0 for d in days]", [d if d > 30 else 0 for d in days], [0, 35, 0, 120, 0])
check("[d // 30 for d in days]", [d // 30 for d in days], [0, 1, 0, 4, 0])
check("[d for d in days if d]", [d for d in days if d], [35, 120, 15])

# =============================================================================
# == Part 3: generator expressions ==
check("sum(1 for d in days if d > 0)", sum(1 for d in days if d > 0), 3)
check("sum(d for d in days if d > 30)", sum(d for d in days if d > 30), 155)
late = (d for d in days if d > 0)
first = sum(late)
second = sum(late)
check("first", first, 170)
check("second", second, 0)

# =============================================================================
# == Part 4: zip and enumerate ==
check('list(zip([1, 2, 3], ["a", "b"]))', list(zip([1, 2, 3], ["a", "b"])), [(1, "a"), (2, "b")])
check("[a + b for a, b in zip([1, 2], [10, 20])]", [a + b for a, b in zip([1, 2], [10, 20])], [11, 22])
check('list(enumerate(["x", "y"], start=1))', list(enumerate(["x", "y"], start=1)), [(1,"x"),(2, "y")])
