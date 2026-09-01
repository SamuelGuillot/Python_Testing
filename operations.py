def apply_booking(club, competition, places_required, bookings_dict):
    club_name = club['name']
    comp_name = competition['name']

    if club_name not in bookings_dict:
        bookings_dict[club_name] = {}
    bookings_dict[club_name][comp_name] = bookings_dict[club_name].get(comp_name, 0) + places_required

    competition['numberOfPlaces'] -= places_required
    club['points'] -= places_required

    return bookings_dict