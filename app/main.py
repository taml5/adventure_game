"""The main class of the program.

Defines the necessary API endpoints given by Flask, and calls the game factory to initialise the game engine. There
are two defined endpoints:
 - the default route '/' loads the webpage through rendering index.html.
 - the route '/execute_command' defines a POST request where the webpage provides a command in JSON format.
   The game engine processes the command and returns a string.
"""

from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(import_name=__name__)
# TODO: write and add GameFactory to initialise game

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
