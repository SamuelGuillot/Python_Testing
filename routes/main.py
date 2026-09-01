from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import save_bookings, save_clubs, save_competitions
from finders import find_club_by_email, find_club_by_name, find_competition_by_name
from operations import apply_booking

main_bp = Blueprint('main', __name__)

clubs = None
competitions = None
bookings = None

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/showSummary', methods=['POST'])
def show_summary():
    club = find_club_by_email(request.form['email'], clubs)
    return render_template('welcome.html', club=club, competitions=competitions)

@main_bp.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = find_club_by_name(club, clubs)
    found_competition = find_competition_by_name(competition, competitions)
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=found_club, competitions=competitions)

@main_bp.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = find_competition_by_name(request.form['competition'], competitions)
    club = find_club_by_name(request.form['club'], clubs)
    places_required = int(request.form['places'])
    apply_booking(club, competition, places_required, bookings)
    save_competitions(competitions)
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

@main_bp.route('/logout')
def logout():
    return redirect(url_for('main.index'))