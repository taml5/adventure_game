"""The main class of the program.

Initialises all the required classes, loads the needed data, and prepares the presenter."""

from flask import Flask, render_template

app = Flask(import_name=__name__)


@app.route('/')
def index():
    """Render the main html webpage on the server."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
