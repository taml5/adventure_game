"""Interprets player input into valid input data for the GameInteractor."""
from engine.gameinteractor import GameInteractor

VALID_COMMANDS = {'help', 'go'}  # TODO: define allowed commands


class Controller:
    """Interprets player input into valid input data for the GameInteractor.

    interactor: the game interactor.
    """
    interactor: GameInteractor

    def __init__(self, interactor: GameInteractor):
        self.interactor = interactor

    def parse_input(self, user_input: str) -> list[str] | None:
        """Given an input string by the player, parse it and execute the associated
        command.
        """
        words = user_input.lower().strip().split()

        if len(words) < 1:
            return self.interactor.handle_invalid_event()
        elif words[0] in VALID_COMMANDS:
            return self.parse_command(words)
        else:
            return self.interactor.handle_invalid_event()

    def parse_command(self, words: list[str]) -> list[str]:
        """Given a valid command, process the given words and execute the corresponding
        GameInteractor method.
        TODO: finish handling for each interaction

        Preconditions:
         - len(words) >= 1
         - words[0] in VALID_COMMANDS
        """
        verb = words[0]

        if verb == 'help':
            return self.interactor.get_help()
        elif verb == 'inventory':
            ...
        elif len(words) > 1:
            if verb == 'go':
                return self.interactor.move_rooms(words[1])
            elif verb == 'take':
                ...
            elif verb == 'drop':
                ...
            elif verb == 'open':
                ...
            elif verb == 'inspect':
                ...
            elif verb == 'use':
                ...
        else:
            return self.interactor.handle_invalid_event()

    def announce_room(self) -> list[str]:
        """Call the appropriate GameInteractor function to return the name and description of the room
        when first initialising the game.
        """
        return self.interactor.announce_room()
