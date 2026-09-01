from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime
from database import save_bookings, save_clubs, save_competitions
from finders import find_club_by_email, find_club_by_name, find_competition_by_name
from validators import is_competition_past, compute_max_places, validate_and_prepare_booking
from operations import apply_booking
from utils import get_now_str

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
    if not club:
        return render_template('index.html', error="Email not found. Please try again.")
    return render_template('welcome.html', club=club, competitions=competitions, now=get_now_str())

@main_bp.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = find_club_by_name(club, clubs)
    found_competition = find_competition_by_name(competition, competitions)

    if not found_club:
        return render_template('index.html', error="Club not found. Please try again."), 404
    if not found_competition:
        return render_template('index.html', error="Competition missing. Please try again."), 404

    if is_competition_past(found_competition, datetime.now()):
        flash("This competition has already taken place.")
        return render_template('welcome.html', club=found_club, competitions=competitions, now=get_now_str())

    max_allowed = compute_max_places(found_club, found_competition, bookings)
    return render_template('booking.html', club=found_club, competition=found_competition, max_places=max_allowed)

@main_bp.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    club = find_club_by_name(request.form['club'], clubs)
    competition = find_competition_by_name(request.form['competition'], competitions)

    if not club or not competition:
        return render_template('index.html', error="Invalid data."), 404

    if is_competition_past(competition, datetime.now()):
        flash("Cannot purchase places for a past competition.")
        return render_template('welcome.html', club=club, competitions=competitions, now=get_now_str())

    try:
        places_required = int(request.form['places'])
    except ValueError:
        flash("Enter a valid number.")
        return render_template('booking.html', club=club, competition=competition)

    is_valid, error_msg, max_allowed = validate_and_prepare_booking(
        club, competition, places_required, bookings, datetime.now()
    )

    if not is_valid:
        flash(error_msg)
        return render_template('booking.html', club=club, competition=competition, max_places=max_allowed)

    apply_booking(club, competition, places_required, bookings)
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions, now=get_now_str())
@main_bp.route('/logout')
def logout():
    return redirect(url_for('main.index'))

@main_bp.route('/points')
def points_display():
    sorted_clubs = sorted(clubs, key=lambda c: c['points'], reverse=True)
    return render_template('points.html', clubs=sorted_clubs)