"""Rooms that a player can move between and interact with its contents.

This class is an entity that serves as the building blocks for the map of the game.
"""
from entities.interaction import Interaction
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
    interactions: a collection of Interactions associated with the room that updates the game state after
                  certain conditions are fulfilled.
    """
    name: str
    description: str
    visited: bool
    contents: dict[int: Item]
    neighbours: dict[str: 'Room']
    interactions: set[Interaction]

    def __int__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.visited = False
        self.contents = {}
        self.neighbours = {}
        self.interactions = set()

    def contains(self, item_id: int) -> bool:
        """Returns whether an item is in the room."""
        return item_id in self.contents

    def add_item(self, item: Item) -> None:
        """Adds an item to the contents of the room."""
        self.contents[item.item_id] = item

    def pop_item(self, item_id: int) -> Item:
        """Remove an item from the contents of the room and return it."""
        return self.contents.pop(item_id)

    def add_neighbour(self, neighbour: 'Room', direction: str) -> None:
        """Attach a neighbour to this room.

        Preconditions
        - direction in DIRECTIONS
        - direction not in self.neighbours
        - DIRECTIONS[direction] not in neighbour.neighbours
        """
        self.neighbours[direction] = neighbour
        neighbour.neighbours[DIRECTIONS[direction]] = self

    def add_neighbours(self, neighbours: dict['Room': str]) -> None:
        """Attach a collection of neighbours to this room.

        Preconditions: all of add_neighbour's preconditiosn hold for each of neighbours
        """
        for room in neighbours:
            self.add_neighbour(room, neighbours[room])

    def add_interaction(self, interaction: Interaction) -> None:
        """Add an interaction that takes place in this room."""
        self.interactions.add(interaction)

    def execute_interaction(self, item: Item) -> tuple[bool, str | None]:
        """Given an item, try to use the item in the room by finding a valid interaction. If found,
        execute it and return a tuple containing True and its output message. Otherwise, return a tuple
        containing False and None.
        """
        for interaction in self.interactions:
            if item in interaction:
                return True, interaction.execute_interaction()

        return False, None
