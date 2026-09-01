from flask import Flask
import database
import routes.main

def create_app():
    app = Flask(__name__)
    app.secret_key = 'something_special'

    clubs = database.load_clubs()
    competitions = database.load_competitions()
    bookings = database.load_bookings()

    routes.main.clubs = clubs
    routes.main.competitions = competitions
    routes.main.bookings = bookings

    app.register_blueprint(routes.main.main_bp)
    return app