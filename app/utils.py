from datetime import datetime


def parse_due_date(date_str):
    # Subtle bug: does not handle ValueError for invalid dates
    return datetime.fromisoformat(date_str)
