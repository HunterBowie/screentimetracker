import datetime


def convert_str_to_date(raw_date: str) -> datetime.date:
    """Converts a date in the form dd/mm/yyyy to a date object."""

    day, month, year = raw_date.split("/")

    day, month, year = int(day), int(month), int(year)

    return datetime.date(year, month, day)
