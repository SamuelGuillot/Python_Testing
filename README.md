# gudlift-registration

1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 
        
    * [pytest](https://docs.pytest.org/)

            This is used for the unit and integration tests in the project.

    * [Locust](https://locust.io/)

            This is used for the performance tests.




3. Installation

   * After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

   * Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

   * Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

   * Flask requires that you set an environmental variable to the python file. In the current version of the project the Flask application is created in <code>app.py</code> and started using <code>run.py</code>.

   * You can start the application by typing <code>python run.py</code>. The app should respond with an address you should be able to go to using your browser.

   * You can also use Flask directly with <code>flask --app run.py run</code>.

4. Current Setup

   The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:

   * competitions.json - list of competitions, including their dates and the number of places available.

   * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

   * bookings.json - stores the current bookings for clubs and competitions.


   The application is split into a few separate files:

   * app.py - creates the Flask application and loads the application data.

   * run.py - starts the Flask application.

   * database.py - handles loading and saving the JSON data.

   * finders.py - contains functions for finding clubs and competitions.

   * operations.py - contains the booking operations, including calculating the maximum number of places and applying a booking.

   * validators.py - contains the validation rules for bookings.

   * utils.py - contains utility functions.

   * routes/main.py - contains the main Flask routes for login, booking, points and logout.

   The main routes currently available are:

   * <code>/</code> - displays the registration/login page.

   * <code>/showSummary</code> - accepts a club email address and displays the club's competitions.

   * <code>/book/<competition>/<club></code> - displays the booking page for a competition and club.

   * <code>/purchasePlaces</code> - processes a booking.

   * <code>/points</code> - displays the club points board.

   * <code>/logout</code> - returns to the home page.

   The application currently has the following booking rules:

   * A competition that has already taken place cannot be booked.

   * The number of places requested must be a valid number.

   * The number of places requested must be positive.

   * A club cannot book more places than are available in the competition.

   * A club cannot book more places than it has points available.

   * A club can book a maximum of 12 places for a competition in total.

   * If a club has already booked places for a competition, the remaining number of places available to that club is reduced accordingly.

   When a booking is successfully completed, the club's points and the competition's available places are updated, and the booking is saved.

5. Testing

   You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

   The project currently uses [pytest](https://docs.pytest.org/) for the unit and integration tests.

   The tests are split into:

   * <code>tests/unit/</code> - tests individual pieces of functionality.

     These currently include tests for:

     * Finding clubs by email.
     * Finding clubs by name.
     * Finding competitions by name.
     * Calculating the maximum number of places that can be booked.
     * Applying a booking.
     * Updating club points.
     * Updating competition places.
     * Validating bookings.
     * Preventing bookings for past competitions.
     * Preventing negative bookings.
     * Enforcing the 12-place limit.

   * <code>tests/integration/</code> - tests the Flask application through its routes.

     These currently include tests for:

     * The index page.
     * Valid club login.
     * Invalid club email addresses.
     * Logging out.
     * Opening a competition booking page.
     * Missing competitions.
     * Missing clubs.
     * Booking a future competition.
     * Booking a past competition.
     * Successful bookings.
     * Insufficient club points.
     * The 12-place limit.
     * Full competitions.
     * Non-numeric booking values.
     * Negative booking values.
     * Invalid clubs and competitions.
     * The club points board.
     * Sorting the points board by points.
     * Links back to the home page.

   The test data is kept separate from the main JSON data. The test fixtures in <code>tests/conftest.py</code> create a Flask test client and reset the clubs, competitions and bookings for each test.

   To run the tests, use:

   <code>pytest</code>

   We also like to show how well we're testing, so there's a module called
   [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

6. Performance Testing

   The project also contains performance tests using [Locust](https://locust.io/).

   The performance test is located in:

   <code>tests/performance/locustfile.py</code>

   The Locust test simulates users who:

   * Log in using a club email address.

   * View the points board.

   * View their summary.

   * Make a valid booking.

   * Attempt an invalid booking.

   The test gives different weights to these activities so that booking places is performed more frequently than some of the other actions.

   The performance test uses dedicated performance-test data. The application checks the <code>PERF_TEST</code> environment variable when it starts.

   To run the application using the performance test data, set:

   <code>PERF_TEST=true</code>

   and then start the application with:

   <code>python run.py</code>

   You can then run Locust using:

   <code>locust -f tests/performance/locustfile.py</code>

   Locust will provide the interface for configuring the number of users and the rate at which they are started.

7. Booking Process

   A booking is processed through the <code>/purchasePlaces</code> route.

   The application:

   * Finds the club and competition.

   * Checks that the requested number of places is valid.

   * Checks that the competition has not already taken place.

   * Checks the maximum number of places that the club is allowed to book.

   * Applies the booking if all validation checks pass.

   * Updates the club's points.

   * Updates the competition's available places.

   * Updates the bookings data.

   * Saves the updated JSON files.

   * Displays a booking confirmation.

   The booking logic is separated into validation and operations so that the individual pieces can also be tested independently.

8. Points Board

   The application includes a points board available at <code>/points</code>.

   Clubs are sorted by their available points, with the club with the most points displayed first.

   The points board currently displays all clubs loaded from <code>clubs.json</code>.

9. Future Improvements

   This is still a proof of concept, so there are a number of areas that could be improved as the project develops.

   Some possible next steps are:

   * Replace the JSON files with a database when one is needed.

   * Add more comprehensive coverage reporting.

   * Improve authentication and session handling.

   * Add additional validation and error handling.

   * Expand the performance tests.

   * Add automated testing to a CI/CD pipeline.

   * Continue to use feedback from users to iterate on the booking platform.

10. Project Structure

    The current project structure is:

    <pre>
    Python_Testing/
    ├── app.py
    ├── run.py
    ├── database.py
    ├── finders.py
    ├── operations.py
    ├── validators.py
    ├── utils.py
    ├── bookings.json
    ├── clubs.json
    ├── competitions.json
    ├── requirements.txt
    │
    ├── routes/
    │   ├── __init__.py
    │   └── main.py
    │
    ├── templates/
    │   ├── booking.html
    │   ├── index.html
    │   ├── points.html
    │   └── welcome.html
    │
    └── tests/
        ├── conftest.py
        ├── integration/
        │   ├── test_booking.py
        │   ├── test_login.py
        │   └── test_points.py
        ├── performance/
        │   └── locustfile.py
        └── unit/
            ├── test_apply_booking.py
            ├── test_finders.py
            ├── test_max_places.py
            └── test_validation.py
    </pre>
