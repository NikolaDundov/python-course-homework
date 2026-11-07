# Homework 3: a portfolio snapshot
# Run: python 03-lists-tuples-sets/homework.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the repository root, where check.py is
from check import check, DATA

# =============================================================================
# == Part 1: read the loans ==
# Read data/loans.csv into loans: a list with one tuple per loan,
#   (loan_id, client_id, product, outstanding, stage)
# outstanding as a float, stage as an int; the others as strings.
# count: the number of loans.

# ---- your code: part 1 ----
loans = []
count = 0


with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                     # the header
    for line in file:
            (loan_id, client_id, product, currency, start_date, maturity_date,
         amount, outstanding, rate, days_past_due, stage) = line.strip().split(",")
            loans.append((loan_id, client_id, product, float(outstanding), int(stage)))
            count += 1
# ---- end of your code ----

check("count", count, 400)
check("loans[:1]", loans[:1], [("L000001", "C0080", "investment", 1044231.3, 1)])

# =============================================================================
# == Part 2: the five largest exposures ==
# Make a list of (outstanding, loan_id) tuples and sort it from the largest:
# tuples are compared by their first item first.
#   top5_ids     the loan_ids of the five largest loans, from the largest (a list)
#   top5_share   their outstanding / the total outstanding, rounded to 4
#                decimals - a simple measure of concentration

# ---- your code: part 2 ----

ids = []
sorted_ids=[]
top5_ids = []
top5_share = 0.0
total_outstanding = 0.0
top5_outstanding = 0.0
all_products = set()
clients_consumers = set()
clients_mortgage = set()
stage3_clients_ids = set()

with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                     # the header
    for line in file:
            (loan_id, client_id, product, currency, start_date, maturity_date,
         amount, outstanding, rate, days_past_due, stage) = line.strip().split(",")
            total_outstanding += float(outstanding)
            ids.append(( float(outstanding), loan_id))
            all_products.add(product)
            if product == "consumer":
                  clients_consumers.add(client_id)
            if product == "mortgage":
                  clients_mortgage.add(client_id)
            if int(stage) == 3:
                  stage3_clients_ids.add(client_id)
            

sorted_ids = sorted(ids, key=lambda x: x[0], reverse=True)
for i in sorted_ids[:5]:
     # print(i)
      top5_ids.append(i[1])
      top5_outstanding += i[0]

top5_share = round(top5_outstanding / total_outstanding,4)
# print(ids)
# ---- end of your code ----

check("top5_ids", top5_ids, ["L000070", "L000246", "L000386", "L000359", "L000351"])
check("top5_share", top5_share, 0.2952)

# =============================================================================
# == Part 3: the products ==
# products: the different products, as a sorted list.

# ---- your code: part 3 ----

products = sorted(list(all_products))
# ---- end of your code ----

check("products", products, ["consumer", "credit_card", "investment", "mortgage", "overdraft",
                             "project_finance", "working_capital"])

# =============================================================================
# == Part 4: clients with a mortgage and a consumer loan ==
# mortgage_and_consumer: the clients that have both a mortgage and a consumer
# loan, as a sorted list.

# ---- your code: part 4 ----
mortgage_and_consumer_set = clients_consumers & clients_mortgage
mortgage_and_consumer = sorted(list(mortgage_and_consumer_set))
# ---- end of your code ----

check("len(mortgage_and_consumer)", len(mortgage_and_consumer), 24)
check("mortgage_and_consumer[:3]", mortgage_and_consumer[:3], ["C0007", "C0035", "C0040"])

# =============================================================================
# == Part 5: the regions of the stage 3 clients ==
# stage_3_regions: the regions (from data/clients.csv) of the clients that have
# a loan in stage 3, as a sorted list without duplicates. This is
#   SELECT DISTINCT region FROM clients
#   WHERE client_id IN (SELECT client_id FROM loans WHERE stage = 3)
# - collect the stage 3 clients into a set first, then read clients.csv.

# ---- your code: part 5 ----
stage_3_regions_set = set()
stage_3_regions = []

with open(DATA / "clients.csv", encoding="utf-8") as file:
    file.readline()                     # the header
    for line in file:
            (client_id,	segment, region, industry, rating, client_since) = line.strip().split(",")
            if client_id in stage3_clients_ids:
                  stage_3_regions_set.add(region)
                  
stage_3_regions = sorted(list(stage_3_regions_set))


# ---- end of your code ----

check("stage_3_regions", stage_3_regions, ["Burgas", "Pleven", "Ruse", "Stara Zagora", "Varna"])
