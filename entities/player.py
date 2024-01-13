"""The player that is controlled and interacts with the world.

TODO: write module docstring
"""
from entities.item import Item
from entities.room import Room


class Player:
    """
    TODO: write docstring
    """
    inventory: dict[int: Item]
    location: Room

    def __init__(self, room: Room):
        self.location = room
        self.inventory = {}  # when player is initialised, inventory should be empty

    def add_item(self, item: Item) -> None:
        """Add an item into the player's inventory."""
        self.inventory[item.id] = item

    def drop_item(self, item: Item) -> None:
        """Remove an item from the player's inventory, and add it to the room.

        Preconditions:
        - item in self.inventory
        """
        self.inventory.pop(item.id)
        self.location.contents[item.id] = Item

    def has_item(self, item_id: int) -> bool:
        """..."""
        return item_id in self.inventory
