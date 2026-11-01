# Task 4: match
# Run: python 02-conditions-and-loops/practice/task4-match.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# == Part 1: product groups ==
# Inside the loop, set group with match:
#   "mortgage", "consumer", "credit_card", "overdraft"       -> "retail"
#   "working_capital", "investment", "project_finance"       -> "business"
#   anything else                                            -> "unknown"
# Use | to put several values in one case.
groups = ""
for product in ["mortgage", "consumer", "credit_card", "overdraft",
                "working_capital", "investment", "project_finance", "leasing"]:
    match product:
        case "mortgage" | "consumer" | "credit_card"| "overdraft":
            group = "retail"
        case  "working_capital" | "investment" | "project_finance":
            group = "business"
        case _:
            group = "unknown"
    # ---- end of your code ----
    groups += f"{group};"

check("groups", groups, "retail;retail;retail;retail;business;business;business;unknown;")

# == Part 2: a currency converter ==
# Bulgaria uses the euro since 2026, at the fixed rate 1 EUR = 1.95583 BGN.
# The loop gives a menu choice and an amount:
#   choice "1": EUR to BGN - result = amount * RATE
#   choice "2": BGN to EUR - result = amount / RATE
#   any other choice: result = "wrong choice"
# For "1" and "2", result is a text with 2 decimals: f"{value:.2f}".
RATE = 1.95583

results = ""
for choice, amount in [("1", 100.0), ("2", 195.58), ("3", 50.0), ("1", 1000.0)]:
    if choice == "1":
        result = f"{amount * RATE:.2f}"
    elif choice == "2":
        result = f"{amount / RATE:.2f}"
    else:
        result = "wrong choice"
    # ---- end of your code ----
    results += f"{result};"

check("results", results, "195.58;100.00;wrong choice;1955.83;")
