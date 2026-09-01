from datetime import datetime

def is_competition_past(competition, current_datetime):
    """Return True if the competition date is before the given datetime."""
    comp_date = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
    return comp_date < current_datetime

def compute_max_places(club, competition, bookings_dict):
    """Return the maximum places a club can still book for a competition."""
    places = competition.get('numberOfPlaces', 0)
    points = club.get('points', 0)
    already_booked = bookings_dict.get(club['name'], {}).get(competition['name'], 0)
    max_places = min(places, points, 12 - already_booked)
    return max(max_places, 0)


def validate_and_prepare_booking(club, competition, places_required, bookings, current_date):
    """Validate a booking request and return (is_valid, error_msg, max_allowed)."""
    if is_competition_past(competition, current_date):
        return False, "Cannot purchase places for a past competition.", 0

    if places_required <= 0:
        return False, "Please enter a positive number of places.", 0

    comp_places = competition['numberOfPlaces']
    club_points = club['points']
    already_booked = bookings.get(club['name'], {}).get(competition['name'], 0)

    max_by_comp = comp_places
    max_by_points = club_points
    max_by_12_rule = 12 - already_booked
    max_allowed = min(max_by_comp, max_by_points, max_by_12_rule)

    if places_required > max_allowed:
        if max_by_comp < places_required:
            return False, f"Not enough places available in the competition (only {max_by_comp} left).", max_allowed
        if max_by_points < places_required:
            return False, f"Your club does not have enough points (you have {club_points}).", max_allowed
        if max_by_12_rule < places_required:
            return False, f"You can only book {max_by_12_rule} more place(s) due to the 12 place limit.", max_allowed
        # fallback
        return False, f"You can only book up to {max_allowed} more places.", max_allowed

    return True, None, max_allowed