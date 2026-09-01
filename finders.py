def find_club_by_email(email, clubs_list):
    """Return the club with the given email, or None if not found."""
    for club in clubs_list:
        if club['email'] == email:
            return club
    return None

def find_club_by_name(name, clubs_list):
    """Return the club with the given name, or None if not found."""
    for club in clubs_list:
        if club['name'] == name:
            return club
    return None

def find_competition_by_name(name, comps_list):
    """Return the competition with the given name, or None if not found."""
    for comp in comps_list:
        if comp['name'] == name:
            return comp
    return None