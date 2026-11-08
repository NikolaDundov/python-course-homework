# Task 5: predict - local and global names, arguments, return values
# Run: python 04-functions/practice/task5-predict-scope.py
#
# Read each small function and the calls after it. Replace each "?" with the
# value you expect, then run the file. It prints OK, WRONG or TODO for each
# prediction, never the real result: run it as often as you like. For a WRONG,
# read the lecture section again and change your prediction. Write the
# prediction in the right type; a function without return gives None.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

x = 10


def f():
    x = 20
    return x


check("f()", f(), 20)
check("x after f()", x, 10)


def g():
    return x * 2


check("g()", g(), 20)


def k(n):
    n = n + 1
    return n


m = 5
check("k(m)", k(m), 6)
check("m after k(m)", m, 5)


def h(items):
    items.append(4)
    return len(items)


numbers = [1, 2, 3]
check("h(numbers)", h(numbers), 4)
check("numbers after h(numbers)", numbers, [1,2,3,4])


def no_return():
    total = 1


check("no_return()", no_return(), None)


def add(a, b=10):
    return a + b


check("add(1)", add(1), 11)
check("add(1, 2)", add(1, 2), 3)
check("add(b=1, a=2)", add(b=1, a=2), 3)


def first_last(*args):
    return args[0], args[-1]


check("first_last(1, 2, 3)", first_last(1, 2, 3), (1,3))

count = 0


def increment():
    global count
    count += 1


increment()
increment()
check("count", count, 2)


def apply(func, value):
    return func(value)


check("apply(len, 'L000001')", apply(len, "L000001"), 7)
