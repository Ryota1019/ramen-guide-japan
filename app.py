# app.py
# This is the main file of the Flask application.
# Flask is a lightweight web framework for Python.
# It handles URL routing — deciding which function runs when a URL is visited.

from flask import Flask, render_template, abort
import data  # Import our restaurant data from data.py

# Create the Flask app instance.
# __name__ tells Flask where to look for templates and static files.
app = Flask(__name__)


# ── Routes ────────────────────────────────────────────────────────────────────
# A "route" connects a URL path to a Python function.
# When a user visits that URL, Flask runs the function and returns the result.

@app.route("/")
def index():
    """Home page — shows an overview and links to city pages."""
    # Get a small preview of restaurants for the home page (first 4)
    featured = data.get_all_restaurants()[:4]
    # render_template() loads the HTML file from the templates/ folder
    # and passes variables into it (featured=featured)
    return render_template("index.html", featured=featured)


@app.route("/tokyo")
def tokyo():
    """Tokyo ramen list page."""
    restaurants = data.get_restaurants_by_city("tokyo")
    # We pass the city name and restaurants into the template
    return render_template("city.html", city="Tokyo", restaurants=restaurants)


@app.route("/osaka")
def osaka():
    """Osaka ramen list page."""
    restaurants = data.get_restaurants_by_city("osaka")
    return render_template("city.html", city="Osaka", restaurants=restaurants)


@app.route("/restaurant/<restaurant_id>")
def detail(restaurant_id):
    """
    Detail page for a single restaurant.
    <restaurant_id> is a dynamic part of the URL.
    For example: /restaurant/ichiran-shinjuku
    Flask captures the value between the < > and passes it as an argument.
    """
    restaurant = data.get_restaurant_by_id(restaurant_id)

    # If the restaurant ID doesn't exist in our data, show a 404 error page
    if restaurant is None:
        abort(404)

    return render_template("detail.html", restaurant=restaurant)


@app.route("/about")
def about():
    """About page — explains the website."""
    return render_template("about.html")


# ── Run the app ───────────────────────────────────────────────────────────────
# This block only runs when you execute this file directly (python app.py).
# It does NOT run when imported as a module.
if __name__ == "__main__":
    # debug=True means Flask will:
    #   1. Show detailed error messages in the browser
    #   2. Automatically reload the server when you save a file
    # IMPORTANT: Never use debug=True on a live production server.
    app.run(debug=True)
