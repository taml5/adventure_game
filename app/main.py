"""The main class of the program.

Initialises all the required classes, loads the needed data, and prepares the presenter."""

from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(import_name=__name__)


@app.route('/')
def index():
    """Render the main html webpage on the server."""
    return render_template('index.html')


@app.route('/execute_command', methods=['POST'])
def execute_command() -> str:
    """Process and attempt to execute the given command via the GameInteractor"""
    if request.method == 'POST':
        command = escape(request.get_json()['input'])
        # TODO: connect game engine to the call
        return f"EXECUTE COMMAND '{command}'"
    else:
        return "ERROR: BAD REQUEST"


if __name__ == "__main__":
    app.run()
