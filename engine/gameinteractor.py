"""The engine of the adventure game.

This contains the GameInteractor that contains the needed logic to manipulate entities, and output the relevant data
to the Presenter to be shown to the player.
"""
from entities.player import Player
from entities.item import Item, Container
from engine.interactor_input_data import InteractorData

VALID_COMMANDS = {"move", "go", "get", "drop"}


class GameInteractor:
    """..."""
    player: Player
    # TODO: add presenter

    def __init__(self, player: Player) -> None:
        self.player = player

    def parse_data(self, input_data: InteractorData):
        """Given some InteractorData, parse the commands and execute the necessary logic."""
        command = input_data.command
        if command not in VALID_COMMANDS:
            return None
        elif command == "move" or command == "go":
            direction = input_data.direction
            self.move_rooms(direction)
        elif command == "get":
            item = input_data.item_ids[0]
            self.pickup_item(item)
        elif command == "drop":
            item = input_data.item_ids[0]
            self.drop_item(item)

    def move_rooms(self, direction: str) -> None:
        """Attempt to move the player into a neighbouring room."""
        neighbouring_rooms = self.player.location.neighbours
        if direction in neighbouring_rooms:
            self.player.location = neighbouring_rooms[direction]
            return None
        else:
            return None

    def pickup_item(self, item_id: int) -> None:
        """Pick an item up from the player's location and place it in the player's inventory.
        """
        item = self.find_item(item_id)
        if item is None:  # item not found
            return None
        elif item[1]:  # item is already in the inventory
            return None
        elif not item[0].portable:  # cannot pick up that item
            return None
        else:
            item = self.player.location.pop_item(item_id)
            if isinstance(item, Container):  # different behaviour if item is a Container
                for subitem in item.contents:
                    self.player.add_item(subitem)
                return None
            else:
                self.player.add_item(item)
                return None

    def drop_item(self, item_id: int) -> None:
        """Attempt to drop an item from the player's inventory. If the player does not have it, do nothing and
        inform the player.
        """
        if self.player.has_item(item_id):
            item = self.player.inventory[item_id]
            self.player.drop_item(item)
            return None
        else:
            return None

    def find_item(self, item_id: int) -> tuple[Item, bool] | None:
        """Find the given item in the player's vicinity (location or inventory). If found, return the item and
        if it is in the player's inventory as a tuple. Otherwise, return None."""
        if self.player.has_item(item_id):
            return (self.player.inventory[item_id], True)
        elif self.player.location.contains(item_id):
            return (self.player.location.contents[item_id], False)
        else:
            return None
