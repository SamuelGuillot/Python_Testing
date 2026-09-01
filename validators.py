from datetime import datetime

def is_competition_past(competition, current_datetime):
    """Return True if the competition date is before the given datetime."""
    comp_date = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
    return comp_date < current_datetime