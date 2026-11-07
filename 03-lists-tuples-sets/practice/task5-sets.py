# Task 5: sets - UNION, INTERSECT, EXCEPT
# Run: python 03-lists-tuples-sets/practice/task5-sets.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: clients in two months ==
# august and september are the clients with a loan at the end of each month.
#   new_clients      in September, not in August (a set)
#   closed_clients   in August, not in September
#   stayed           in both months
#   all_count        how many different clients in the two months (int)
#   changed          new or closed - one operator (a set)
august = {"C0001", "C0002", "C0003", "C0005", "C0008", "C0013"}
september = {"C0002", "C0003", "C0005", "C0013", "C0021", "C0034"}

# ---- your code: part 1 ----
new_clients = september - august
closed_clients = august - september
stayed = august & september
all_count = len(august | september)
changed = new_clients | closed_clients
# ---- end of your code ----

check("new_clients", new_clients, {"C0021", "C0034"})
check("closed_clients", closed_clients, {"C0001", "C0008"})
check("stayed", stayed, {"C0002", "C0003", "C0005", "C0013"})
check("all_count", all_count, 8)
check("changed", changed, {"C0001", "C0008", "C0021", "C0034"})

# =============================================================================
# == Part 2: the documents of a credit file ==
# A credit file needs the documents in required; the client gave submitted.
#   missing          the required documents that were not given (a set)
#   extra            the given documents that are not required (a set)
#   complete         True when every required document was given - use <=
required = {"id_card", "income_statement", "collateral_valuation", "insurance"}
submitted = {"id_card", "insurance", "bank_statement", "income_statement"}

# ---- your code: part 2 ----
missing = required - submitted
extra = submitted - required
complete = required <= submitted
# ---- end of your code ----

check("missing", missing, {"collateral_valuation"})
check("extra", extra, {"bank_statement"})
check("complete", complete, False)

# =============================================================================
# == Part 3: distinct values ==
# products has duplicates.
#   distinct_count   the number of different products (int)
#   distinct_sorted  the different products as a sorted LIST
products = ["consumer", "mortgage", "consumer", "overdraft", "mortgage", "credit_card", "consumer"]

# ---- your code: part 3 ----
distinct_count = len(set(products))
distinct_sorted = sorted(set(products))
# ---- end of your code ----

check("distinct_count", distinct_count, 4)
check("distinct_sorted", distinct_sorted, ["consumer", "credit_card", "mortgage", "overdraft"])
