# Task 5: dates from text
# Run: python 07-text-and-regex/practice/task5-dates.py
#
# In this task a "date" is a datetime.date object, for example date(2026, 9, 30).

from datetime import date, datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: an ISO date ==
# from_iso(text)      the text of a date in the ISO format "2014-06-08" -> a
#     date: date(2014, 6, 8)

# ---- your code: part 1 ----
def from_iso(text):
    return None
# ---- end of your code ----

check('from_iso("2014-06-08")', from_iso("2014-06-08"), date(2014, 6, 8))

# =============================================================================
# == Part 2: a Bulgarian date ==
# from_bg(text)       the text of a date in the format "08.06.2014" (day,
#     month, year) -> a date: date(2014, 6, 8). The result must be a date, not
#     a datetime.

# ---- your code: part 2 ----
def from_bg(text):
    return None
# ---- end of your code ----

check('from_bg("08.06.2014")', from_bg("08.06.2014"), date(2014, 6, 8))
check('from_bg("30.09.2026")', from_bg("30.09.2026"), date(2026, 9, 30))

# =============================================================================
# == Part 3: a date as text ==
# to_bg(d)            a date -> its text in the format "08.06.2014"
# to_month(d)         a date -> the year and the month as text: "2014-06"

# ---- your code: part 3 ----
def to_bg(d):
    return ""

def to_month(d):
    return ""
# ---- end of your code ----

check("to_bg(date(2026, 9, 30))", to_bg(date(2026, 9, 30)), "30.09.2026")
check("to_month(date(2014, 6, 8))", to_month(date(2014, 6, 8)), "2014-06")

# =============================================================================
# == Part 4: is the loan overdue? ==
# is_overdue(due_text, report_date)   due_text is the text of the due date
#     in the format "15.09.2026"; report_date is a date. Return True when the
#     due date is before report_date. Dates compare like numbers: the earlier
#     date is the smaller one.
REPORT_DATE = date(2026, 9, 30)

# ---- your code: part 4 ----
def is_overdue(due_text, report_date):
    return None
# ---- end of your code ----

check('is_overdue("15.09.2026", REPORT_DATE)', is_overdue("15.09.2026", REPORT_DATE), True)
check('is_overdue("30.09.2026", REPORT_DATE)', is_overdue("30.09.2026", REPORT_DATE), False)
check('is_overdue("05.10.2026", REPORT_DATE)', is_overdue("05.10.2026", REPORT_DATE), False)

# =============================================================================
# == Part 5: whole years ==
# years_as_client(since_text, report_date)   since_text is an ISO date text,
#     report_date is a date. Return the number of WHOLE years from since_text
#     to report_date (an int), counted like an age: the year is whole only
#     when the month and the day of since_text have come in the year of
#     report_date. Hint: tuples compare item by item, so
#     (report_date.month, report_date.day) < (d.month, d.day) is True when
#     that day has not come yet.

# ---- your code: part 5 ----
def years_as_client(since_text, report_date):
    return None
# ---- end of your code ----

check('years_as_client("2014-06-08", REPORT_DATE)', years_as_client("2014-06-08", REPORT_DATE), 12)
check('years_as_client("2016-09-30", REPORT_DATE)', years_as_client("2016-09-30", REPORT_DATE), 10)
check('years_as_client("2016-10-01", REPORT_DATE)', years_as_client("2016-10-01", REPORT_DATE), 9)
