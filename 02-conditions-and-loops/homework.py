# Homework 2: a report of days past due
# Run: python 02-conditions-and-loops/homework.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the repository root, where check.py is
from check import check, DATA

# == Part 1: the buckets ==
# Read data/loans.csv (as in task 5) and put every loan into one of four buckets
# by its days_past_due: "current" (0), "1-30", "31-90", "90+".
# For each bucket, the number of loans and the sum of outstanding:
#   current_count, late_30_count, late_90_count, over_90_count       (int)
#   current_total, late_30_total, late_90_total, over_90_total       (float,
#   rounded to 2 decimals after the loop)

# ---- your code: part 1 ----
current_count = late_30_count = late_90_count = over_90_count = 0
current_total = late_30_total = late_90_total = over_90_total = 0.0

with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                     # the header
    for line in file:
        (loan_id, client_id, product, currency, start_date, maturity_date,
         amount, outstanding, rate, days_past_due, stage) = line.strip().split(",")
        if int(days_past_due)==0:
            current_count += 1
            current_total += float(outstanding)
        elif int(days_past_due)>0 and int(days_past_due) <=30:
            late_30_count += 1
            late_30_total += float(outstanding)
        elif int(days_past_due)>30 and int(days_past_due) <=90:
            late_90_count += 1
            late_90_total += float(outstanding)
        elif int(days_past_due)>90:
            over_90_count += 1
            over_90_total += float(outstanding)

# ---- end of your code ----

check("current_count", current_count, 346)
check("late_30_count", late_30_count, 28)
check("late_90_count", late_90_count, 9)
check("over_90_count", over_90_count, 17)
check("current_total", current_total, 121748635.18)
check("late_30_total", late_30_total, 3279532.15)
check("late_90_total", late_90_total, 2043507.62)
check("over_90_total", over_90_total, 4299033.65)

# == Part 2: the total and the share over 90 days ==
# total: the sum of all outstanding, rounded to 2 decimals;
# over_90_share: over_90_total / total, rounded to 4 decimals.

# ---- your code: part 2 ----
total = 0.0
total_over_90=0.0
over_90_share = 0.0


with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                     # the header
    for line in file:
        (loan_id, client_id, product, currency, start_date, maturity_date,
         amount, outstanding, rate, days_past_due, stage) = line.strip().split(",")
        total+=float(outstanding)
        if int(days_past_due)>90:
            total_over_90 += float(outstanding)
over_90_share = round(total_over_90/total,4)
      
# ---- end of your code ----

check("total", total, 131370708.6)
check("over_90_share", over_90_share, 0.0327)

# == Part 3: the largest late loan ==
# The largest LATE loan (days_past_due > 0) by outstanding, with one more loop
# over the file:
#   largest_late_id (str), largest_late_amount (float), largest_late_days (int)

# ---- your code: part 3 ----
largest_late_id = ""
largest_late_amount = 0.0
largest_late_days = 0

with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                     # the header
    for line in file:
        (loan_id, client_id, product, currency, start_date, maturity_date,
         amount, outstanding, rate, days_past_due, stage) = line.strip().split(",")
        if int(days_past_due)>largest_late_days:
            largest_late_days = int(days_past_due)


with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                     # the header
    for line in file:
        (loan_id, client_id, product, currency, start_date, maturity_date,
         amount, outstanding, rate, days_past_due, stage) = line.strip().split(",")
        if largest_late_days == int(days_past_due):
            if largest_late_amount < float(outstanding):
                largest_late_amount = float(outstanding)
                largest_late_id = loan_id

# ---- end of your code ----

check("largest_late_id", largest_late_id, "L000103")
check("largest_late_amount", largest_late_amount, 1237517.53)
check("largest_late_days", largest_late_days, 200)

# == Part 4: the report ==
# report: one string of 6 lines, exactly as in the check below: a header,
# one line per bucket, and a total line. Each line: the bucket name left in 8
# characters, the count right in 6, the outstanding right in 18 with a thousands
# separator and 2 decimals, the share right in 8 as a percent with 1 decimal.
# The lines are joined with "\n" (no "\n" at the end). Print it.

# ---- your code: part 4 ----
current_bucket = bucket_1 = bucket_2 = bucket_3 = total_loans = 0
current_outstanding = bucket_1_outstanding= bucket_2_outstanding = bucket_3_outstanding = total_outstanding = 0.0
current_share = bucket_1_share = bucket_2_share = bucket_3_share = 0.0


with open(DATA / "loans.csv", encoding="utf-8") as file:
    file.readline()                     # the header
    for line in file:
        (loan_id, client_id, product, currency, start_date, maturity_date,
         amount, outstanding, rate, days_past_due, stage) = line.strip().split(",")
        if int(days_past_due)==0:
            current_bucket += 1
            current_outstanding += float(outstanding)
        elif int(days_past_due)>0 and int(days_past_due) <=30:
            bucket_1 += 1
            bucket_1_outstanding += float(outstanding)
        elif int(days_past_due)>30 and int(days_past_due) <=90:
            bucket_2 += 1
            bucket_2_outstanding += float(outstanding)
        elif int(days_past_due)>90:
            bucket_3 += 1
            bucket_3_outstanding += float(outstanding)
        total_loans += 1
        total_outstanding += float(outstanding)

        report = (
        f"{'bucket':<8}{'loans':>6}{'outstanding':>18}{'share':>8}\n"
        f"{'current':<8}{current_bucket:>6}{current_outstanding:>18,.2f}{current_outstanding/total_outstanding:>8.1%}\n"
        f"{'1-30':<8}{bucket_1:>6}{bucket_1_outstanding:>18,.2f}{bucket_1_outstanding/total_outstanding:>8.1%}\n"
        f"{'31-90':<8}{bucket_2:>6}{bucket_2_outstanding:>18,.2f}{bucket_2_outstanding/total_outstanding:>8.1%}\n"
        f"{'90+':<8}{bucket_3:>6}{bucket_3_outstanding:>18,.2f}{bucket_3_outstanding/total_outstanding:>8.1%}\n"
        f"{'total':<8}{total_loans:>6}{total_outstanding:>18,.2f}{100.0:>7.1f}%"
    )

print(report)

# ---- end of your code ----

check("report", report,
      "bucket   loans       outstanding   share\n"
      "current    346    121,748,635.18   92.7%\n"
      "1-30        28      3,279,532.15    2.5%\n"
      "31-90        9      2,043,507.62    1.6%\n"
      "90+         17      4,299,033.65    3.3%\n"
      "total      400    131,370,708.60  100.0%")
