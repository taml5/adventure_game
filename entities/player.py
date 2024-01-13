"""The player that is controlled by the user and interacts with the world.
"""
from entities.item import Item, Container
from entities.room import Room


class Player:
    """
    Class representing the player.

    inventory: the player's inventory. This is represented as a dictionary of the item id, and the item. inventory
               cannot contain Containers.
    location: the player's current location.
    """
    inventory: dict[int: Item]
    location: Room

    def __init__(self, room: Room):
        self.location = room
        self.inventory = {}

    def add_item(self, item: Item) -> None:
        """Add an item into the player's inventory. If the item is a container, then recursively add its
        items into the player's inventory.
        """
        if isinstance(item, Container):
            # output something here about the container
            for container_item in item.contents.values:
                self.add_item(container_item)
            return None
        else:
            self.inventory[item.item_id] = item
            return None

    def drop_item(self, item: Item) -> None:
        """Remove an item from the player's inventory, and add it to the room.

        Preconditions:
        - item in self.inventory
        """
        self.inventory.pop(item.item_id)
        self.location.contents[item.item_id] = Item

    def has_item(self, item_id: int) -> bool:
        """Returns if the player has the item."""
        return item_id in self.inventory
