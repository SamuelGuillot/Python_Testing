def apply_booking(club, competition, places_required, bookings_dict): 
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    return bookings_dict