# Homework 4: a library of portfolio functions
# Run: python 04-functions/homework.py
#
# Write the functions below. Each one has a docstring that says what it returns;
# none of them prints. The files are in the data/ folder: DATA / "loans.csv".

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the repository root, where check.py is
from check import check, DATA

# =============================================================================
# == Part 1: read the loans ==
# read_loans(path)    a list of tuples, one per loan:
#                     (loan_id, client_id, product, outstanding, days_past_due, stage)
#                     outstanding a float, days_past_due and stage int

# ---- your code: part 1 ----
def read_loans(path):
    """The loans of the file: (loan_id, client_id, product, outstanding, days_past_due, stage)."""
    return []
# ---- end of your code ----

loans = read_loans(DATA / "loans.csv")
check("len(loans)", len(loans), 400)
check("loans[1:2]", loans[1:2], [("L000002", "C0132", "investment", 651927.3, 35, 2)])

# =============================================================================
# == Part 2: read the ratings ==
# read_ratings(path)  from clients.csv: a list of tuples (client_id, rating),
#                     rating an int

# ---- your code: part 2 ----
def read_ratings(path):
    """The clients of the file: (client_id, rating)."""
    return []
# ---- end of your code ----

ratings = read_ratings(DATA / "clients.csv")
check("len(ratings)", len(ratings), 150)
check("ratings[:1]", ratings[:1], [("C0001", 3)])

# =============================================================================
# == Part 3: read the rating scale ==
# read_rating_scale(path)  from rating_scale.csv: a list of tuples
#                     (rating, grade, pd_min, pd_max) - int, str, float, float

# ---- your code: part 3 ----
def read_rating_scale(path):
    """The rating scale: (rating, grade, pd_min, pd_max)."""
    return []
# ---- end of your code ----

scale = read_rating_scale(DATA / "rating_scale.csv")
check("scale[3:4]", scale[3:4], [(4, "BBB", 0.0025, 0.006)])

# =============================================================================
# == Part 4: the PD of a rating ==
# pd_for_rating(rating, scale)
#     the PD of a rating: the middle of its band, (pd_min + pd_max) / 2.
#     None if the rating is not in the scale.

# ---- your code: part 4 ----
def pd_for_rating(rating, scale):
    """The middle of the PD band of the rating, or None."""
    pass
# ---- end of your code ----

check("pd_for_rating(4, scale)", pd_for_rating(4, scale), 0.00425)
check("pd_for_rating(10, scale)", pd_for_rating(10, scale), 1.0)
check("pd_for_rating(11, scale)", pd_for_rating(11, scale), None)

# =============================================================================
# == Part 5: the rating of a client ==
# rating_of(client_id, ratings)
#     the rating of a client, found with a loop; None if the client is not in
#     the list. (Session 6 does this much faster with a dictionary.)

# ---- your code: part 5 ----
def rating_of(client_id, ratings):
    """The rating of the client, or None."""
    pass
# ---- end of your code ----

check('rating_of("C0132", ratings)', rating_of("C0132", ratings), 7)
check('rating_of("C9999", ratings)', rating_of("C9999", ratings), None)

# =============================================================================
# == Part 6: the expected loss ==
# expected_loss(pd_value, ead, lgd=0.45)
#     EL = PD * LGD * EAD (not rounded)

# ---- your code: part 6 ----
def expected_loss(pd_value, ead, lgd=0.45):
    """EL = PD * LGD * EAD."""
    pass
# ---- end of your code ----

check("expected_loss(0.07, 651927.30)", expected_loss(0.07, 651927.30), 20535.70995)
check("expected_loss(0.02, 100000, lgd=0.25)", expected_loss(0.02, 100000, lgd=0.25), 500.0)

# =============================================================================
# == Part 7: the expected loss of the portfolio ==
# portfolio_el(loans, ratings, scale, lgd=0.45)
#     the sum of the expected loss of all loans: the PD comes from the rating of
#     the client of each loan, the EAD is the outstanding amount. Rounded to 2
#     decimals. Use your other functions!

# ---- your code: part 7 ----
def portfolio_el(loans, ratings, scale, lgd=0.45):
    """The expected loss of all loans, rounded to 2 decimals."""
    pass
# ---- end of your code ----

check("portfolio_el(loans, ratings, scale)", portfolio_el(loans, ratings, scale), 1140106.56)

# =============================================================================
# == Part 8: totals by stage ==
# totals_by_stage(loans)  a tuple of three sums of outstanding: stage 1, 2, 3,
#                         each rounded to 2 decimals
# Hint: three accumulators, one per stage, and if / elif in the loop - as the
# buckets of homework 2.

# ---- your code: part 8 ----
def totals_by_stage(loans):
    """The outstanding of stage 1, 2 and 3, each rounded to 2 decimals."""
    pass
# ---- end of your code ----

check("totals_by_stage(loans)", totals_by_stage(loans), (110184825.28, 16884527.04, 4301356.28))
