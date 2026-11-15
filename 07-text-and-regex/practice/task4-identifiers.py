# Task 4: clean identifiers
# Run: python 07-text-and-regex/practice/task4-identifiers.py
#
# Each function takes the raw text and returns the clean value, or None if the
# value cannot be cleaned.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # the repository root, where check.py is
from check import check

# =============================================================================
# == Part 1: a client id ==
# clean_client_id(raw)  "C" and 4 digits: remove spaces and "-", upper case,
#     pad the number with zeros: "c 17" -> "C0017". None if it is not a C
#     followed by digits, or if the number has more than 4 digits.

# ---- your code: part 1 ----
def clean_client_id(raw):
    return None
# ---- end of your code ----

check('clean_client_id("c 17")', clean_client_id("c 17"), "C0017")
check('clean_client_id(" C-0026")', clean_client_id(" C-0026"), "C0026")
check('clean_client_id("C0001")', clean_client_id("C0001"), "C0001")
check('clean_client_id("X0001")', clean_client_id("X0001"), None)
check('clean_client_id("C12345")', clean_client_id("C12345"), None)

# =============================================================================
# == Part 2: an EIK ==
# clean_eik(raw)        digits only: remove spaces and a "BG" in front (any
#     case). 9 or 13 digits, else None.

# ---- your code: part 2 ----
def clean_eik(raw):
    return None
# ---- end of your code ----

check('clean_eik("BG 165 960 351")', clean_eik("BG 165 960 351"), "165960351")
check('clean_eik("bg1965730713386")', clean_eik("bg1965730713386"), "1965730713386")
check('clean_eik("12345678")', clean_eik("12345678"), None)

# =============================================================================
# == Part 3: an IBAN ==
# clean_iban(raw)       no spaces, upper case; 22 characters, starts with "BG",
#     only letters and digits, else None. An empty value gives None.

# ---- your code: part 3 ----
def clean_iban(raw):
    return None
# ---- end of your code ----

check('clean_iban("bg05 test 7701 8249 4644 61")', clean_iban("bg05 test 7701 8249 4644 61"), "BG05TEST77018249464461")
check('clean_iban("")', clean_iban(""), None)
check('clean_iban("DE89370400440532013000")', clean_iban("DE89370400440532013000"), None)

# =============================================================================
# == Part 4: an e-mail ==
# clean_email(raw)      no spaces at the ends, lower case; exactly one "@",
#     something before it, a "." after it, and no spaces inside - else None.

# ---- your code: part 4 ----
def clean_email(raw):
    return None
# ---- end of your code ----

check('clean_email(" Yana.Koleva@Example.org")', clean_email(" Yana.Koleva@Example.org"), "yana.koleva@example.org")
check('clean_email("office at example.net")', clean_email("office at example.net"), None)
check('clean_email("@example.net")', clean_email("@example.net"), None)
check('clean_email("a@@b.c")', clean_email("a@@b.c"), None)

# =============================================================================
# == Part 5: clean a whole column ==
# clean_column(values, cleaner)  a function: applies a cleaner to a list of raw
#     values and returns a tuple (clean_values, changed, invalid): changed =
#     how many clean values differ from the raw value (None counts as
#     invalid, not as changed), invalid = how many are None.

# ---- your code: part 5 ----
def clean_column(values, cleaner):
    return [], 0, 0
# ---- end of your code ----

check('clean_column(["C1", "c0002", "x"], clean_client_id)', clean_column(["C1", "c0002", "x"], clean_client_id),
      (["C0001", "C0002", None], 2, 1))
