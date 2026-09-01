from datetime import datetime

def is_competition_past(competition, current_datetime):
    """Return True if the competition date is before the given datetime."""
    comp_date = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
    return comp_date < current_datetime

def compute_max_places(club, competition, bookings_dict):
    """Return the maximum places a club can still book for a competition."""
    places = int(competition.get('numberOfPlaces', 0))
    points = int(club.get('points', 0))
    already_booked = bookings_dict.get(club['name'], {}).get(competition['name'], 0)
    max_places = min(places, points, 12 - already_booked)
    return max(max_places, 0)