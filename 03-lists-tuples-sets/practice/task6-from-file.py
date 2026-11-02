# Task 6: lists and sets from the data files
# Run: python 03-lists-tuples-sets/practice/task6-from-file.py
#
# Read data/loans.csv and data/clients.csv line by line (as in session 2 - skip
# the header line, split each line by ","). The columns:
#   loans.csv    loan_id,client_id,product,currency,start_date,
#                maturity_date,amount,outstanding,interest_rate,days_past_due,stage
#   clients.csv  client_id,segment,region,industry,rating,client_since

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check, DATA

# =============================================================================
# == Part 1: from loans.csv ==
# In one loop over loans.csv:
#   products         the different products, as a sorted list
#   stage_3_ids      the loan_ids of the stage 3 loans, a list in the order of the file
#   first_five       the first five of stage_3_ids (a slice)
#   late_clients     the client_ids with a loan more than 90 days past due (a set)
#   both_currencies  the client_ids with a loan in EUR AND a loan in USD (a set:
#                    collect the EUR clients and the USD clients, then intersect)
# Collect also the client_ids of all loans in a set - you need it in part 2.

# ---- your code: part 1 ----
products = None
stage_3_ids = []
first_five = None
late_clients = None
both_currencies = set()
# ---- end of your code ----

check("products", products, ["consumer", "credit_card", "investment", "mortgage", "overdraft",
                             "project_finance", "working_capital"])
check("len(stage_3_ids)", len(stage_3_ids), 19)
check("first_five", first_five, ["L000012", "L000014", "L000025", "L000059", "L000077"])
check("late_clients", late_clients, {"C0008", "C0016", "C0020", "C0039", "C0040", "C0047", "C0075",
                                     "C0079", "C0090", "C0100", "C0119", "C0132", "C0144"})
check("len(both_currencies)", len(both_currencies), 31)
check('"C0132" in both_currencies', "C0132" in both_currencies, True)

# =============================================================================
# == Part 2: from clients.csv ==
# In one loop over clients.csv:
#   regions          the different regions, as a sorted list
#   without_loans    the client_ids of clients.csv that have no loan, as a sorted
#                    list (like SELECT ... EXCEPT SELECT ...) - use the set of
#                    the client_ids of the loans from part 1

# ---- your code: part 2 ----
regions = None
without_loans = None
# ---- end of your code ----

check("regions", regions, ["Burgas", "Pleven", "Plovdiv", "Ruse", "Sofia", "Stara Zagora", "Varna"])
check("without_loans", without_loans, ["C0005", "C0006", "C0091", "C0118", "C0131", "C0140", "C0142"])
