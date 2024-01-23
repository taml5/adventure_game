"""Rooms that a player can move between and interact with its contents.

This class is an entity that serves as the building blocks for the map of the game.
"""
from entities.item import Item

DIRECTIONS = {"north": "south", "east": "west", "south": "north", "west": "east",
              "up": "down", "down": "up"}


class Room:
    """A room that the player can traverse and interact with.

    name: the name of the room.
    description: a description of the room.
    visited: whether if the player has already visited this room or not.
    contents: a dictionary of item ids and the item that it contains.
    neighbours: a dictionary of directions and a connected room in that direction that the player can move to.
    """
    name: str
    description: str
    visited: bool
    contents: dict[int: Item]
    neighbours: dict[str: 'Room']

    def __int__(self):
        self.name = ''
        self.description = ''
        self.visited = False
        self.contents = {}
        self.neighbours = {}

    def contains(self, item_id: int) -> bool:
        """Returns whether an item is in the room."""
        return item_id in self.contents

    def add_item(self, item: Item) -> None:
        """Adds an item to the contents of the room."""
        self.contents[item.item_id] = item

    def pop_item(self, item_id: int) -> Item:
        """Remove an item from the contents of the room and return it."""
        return self.contents.pop(item_id)

    def add_neighbour(self, neighbour: 'Room', direction: str):
        """Add a neighbour to this room.

        Preconditions
        - direction in DIRECTIONS
        - direction not in self.neighbours
        - DIRECTIONS[direction] not in neighbour.neighbours
        """
        self.neighbours[direction] = neighbour
        neighbour.neighbours[DIRECTIONS[direction]] = self
