from datetime import datetime, date, timedelta


def even_date_in_month(input_date: date) -> list[datetime]:
    """
    This function get date and return list with even datetime in the same month than date.
    """

    number_days = date(input_date.year + int(input_date.month / 12), input_date.month % 12 + 1, 1) - timedelta(days=1)
    return [datetime.strptime(str(f"{day}, {input_date.month}, {input_date.year}"), "%d, %m, %Y") for day in
            range(1, number_days.day + 1) if not day & 1]


# E.g.
print(even_date_in_month(date.today()))
