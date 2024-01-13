"""Rooms that a player can move between and interact with its contents.

This class is an entity that serves as the building blocks for the map of the game.
"""
from entities.item import Item


class Room:
    """TODO: write docstring"""
    name: str
    description: str
    visited: bool
    contents: dict[int: Item]
    neighbours: dict[int: 'Room']

    def contains(self, item_id: int) -> bool:
        """Returns whether an item is in the room."""
        return item_id in self.contents

    def add_item(self, item: Item) -> None:
        """Adds an item to the contents of the room."""
        self.contents[item.item_id] = item

    def pop_item(self, item_id: int) -> Item:
        """Remove an item from the contents of the room and return it."""
        return self.contents.pop(item_id)
