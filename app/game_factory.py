"""Factory that initialises the game engine."""
from engine.controller import Controller
from engine.gameinteractor import GameInteractor
from entities.player import Player
import data.test_data as data


def initialise() -> Controller:
    """Initialise the engine."""
    player = Player(data.TEST_ROOM1)
    interactor = GameInteractor(player)

    return Controller(interactor)
