def find_club_by_email(email, clubs_list):
    for club in clubs_list:
        if club['email'] == email:
            return club
    return None

def find_club_by_name(name, clubs_list):
    for club in clubs_list:
        if club['name'] == name:
            return club
    return None

def find_competition_by_name(name, competitions_list):
    for comp in competitions_list:
        if comp['name'] == name:
            return comp
    return None