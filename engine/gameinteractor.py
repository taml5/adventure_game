"""The engine of the adventure game.

TODO: write module docstring
"""
from entities.player import Player
from entities.item import Container


class GameInteractor:
    """..."""
    player: Player
    # TODO: add presenter

    def __init__(self, player: Player) -> None:
        self.player = player

    def move_rooms(self, direction: str) -> None:
        """Attempt to move the player into a neighbouring room."""
        neighbouring_rooms = self.player.location.neighbours
        if direction in neighbouring_rooms:
            self.player.location = neighbouring_rooms[direction]
            return None
        else:
            return None

    def pickup_item(self, item_id: int) -> None:
        """Pick an item up from the player's location"""
        if self.player.has_item(item_id):
            return None

        location = self.player.location
        if location.contains(item_id):
            item = location.pop_item(item_id)
            if isinstance(item, Container):  # different behaviour if item is a Container
                return None
            else:
                self.player.add_item(item)
                return None
        else:
            return None

    def drop_item(self, item_id: int) -> None:
        """..."""
        if self.player.has_item(item_id):
            item = self.player.inventory[item_id]
            self.player.drop_item(item)
            return None
        else:
            return None
