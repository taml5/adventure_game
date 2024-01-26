"""The main class of the program.

Defines the necessary API endpoints given by Flask, and calls the game factory to initialise the game engine. There
are two defined endpoints:
 - the default route '/' loads the webpage through rendering index.html.
 - the route '/execute_command' defines a POST request where the webpage provides a command in JSON format.
   The game engine processes the command and returns a string.
"""
from flask import Flask, render_template, request, jsonify
from markupsafe import escape

import game_factory

app = Flask(import_name=__name__)
controller = game_factory.initialise()


@app.route('/')
def index():
    """Render the main html webpage on the server."""
    return render_template('index.html')


@app.route('/on_load', methods=['POST'])
def on_load():
    """Render API text on page load."""
    return jsonify(controller.announce_room())


@app.route('/execute_command', methods=['POST'])
def execute_command():
    """Process and attempt to execute the given command via the GameInteractor"""
    if request.method == 'POST':
        command = escape(request.get_json()['input'])
        return jsonify(controller.parse_input(command))
    else:
        return "ERROR: BAD REQUEST"


if __name__ == "__main__":
    app.run()
