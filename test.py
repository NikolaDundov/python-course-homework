import re

PATTERNS = {
    "loan_id":   r"L\d{6}",
    "client_id": r"C\d{4}",
    "eik":       r"\d{9}|\d{13}",
    "iban_bg":   r"BG\d{2}[A-Z]{4}\d{6}[A-Z0-9]{8}",
    "date_bg":   r"\d{2}\.\d{2}\.\d{4}",
    "email":     r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}",
}

tests = {"loan_id": ["L000001", "L00001", "l000001"],
         "eik": ["175591301", "1965730713386", "12345678901"],
         "iban_bg": ["BG05TEST77018249464461", "BG05 TEST 7701", "DE89370400440532013000"],
         "date_bg": ["30.09.2026", "2026-09-30", "3.9.2026"],
         "email": ["yana.koleva@example.org", "office at example.net", "a@b"]}

for name, values in tests.items():
    for value in values:
        print(f"{name:<9}{value:<26}{bool(re.fullmatch(PATTERNS[name], value))}")