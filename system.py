"""This module contains the Room class, Item class, and Player class, as well as their respective methods."""

from typing import Optional


################################################################
# ITEMS
################################################################


class Item:
    """Items in the game that the player can interact with.

    name: The name of the item.
    keywords: A list of strings that refer to the same item by different names.
    description: A description of the item.
    interactble: If the player can interact with the item or not.
    portable: If the item can be put into the inventory or not.
    hidden: If the item is hidden from the player or not.
    """
    name: str
    keywords: set[str]
    description: str
    interactable: bool
    portable: bool
    hidden: bool

    def __init__(self, name: str, keywords: set[str], description: str, interactable: bool, portable: bool) -> None:
        """Initialise a new Item instance."""
        self.name = name
        self.keywords = keywords
        self.description = description
        self.interactable = interactable
        self.portable = portable
        self.hidden = False


class Container(Item):
    """Subclass of Items that represents a container that can contain items.

    contents: A list of Items that are contained within the container.
    locked: Whether the container is locked and requires a key or not.
    key: An Item that, when used with the container, unlocks the container.
    """
    contents: set[Item]
    locked: bool
    key: Optional[Item] = None

    def __init__(self, name: str, keywords: set[str], description: str, interactable: bool, portable: bool,
                 contents: set[Item], locked: bool, key: Optional[Item] = None) -> None:
        """Initialise a new Container instance."""
        self.contents = contents
        self.locked = locked
        self.key = key
        self.interactable = True
        Item.__init__(self, name, keywords, description, interactable, portable)  # call superclass initialiser

    def display_contents(self) -> None:
        """Print the contents of the container to the player. If there is nothing inside the container,
        tell the player.
        """
        if not self.contents:  # if self.contents == []
            print(f'The {self.name.lower()} is empty.')
        else:
            print(f'The {self.name.lower()} contains: ')
            for item in self.contents:
                print(f'    {item.name}')

    def unlock_container(self, key: Item) -> None:
        """Attempt to unlock the container with the given item. If it is already unlocked, tell the player. If the
        key is correct, unlock the container. Else, tell the player the key doesn't work.
        """
        if not self.locked:
            print('It doesn\'t seem to be locked.')
        elif key.name == self.key.name:
            self.locked = False
            print(f'The {self.name.lower()} unlocks. \n')
            self.display_contents()
        else:
            print(f'The key doesn\'t seem to fit.')


################################################################
# ROOM
################################################################


class Room(Container):
    """Place that the player can visit. Each room can have items.

    name: The name of the place.
    description: A description of the place.
    visited: If the player has visited this place previously.
    neighbours: Other places which this place is connected to.
    contents: A list of Items that the place contains.
    """
    name: str
    description: str
    keywords: set[str]
    visited: bool
    contents: set[Item]
    north: Optional['Room'] = None
    east: Optional['Room'] = None
    south: Optional['Room'] = None
    west: Optional['Room'] = None

    def __init__(self, name: str, description: str, contents: set[Item],
                 north: Optional['Room'] = None, east: Optional['Room'] = None, south: Optional['Room'] = None,
                 west: Optional['Room'] = None) -> None:
        """Initialise a new Room instance."""
        self.visited = False
        Container.__init__(self, name=name, keywords=set(), description=description, interactable=False,
                           portable=False, contents=contents, locked=False, key=None)
        # TODO: investigate possibility of adding locked rooms
        self.north = north
        self.east = east
        self.south = south
        self.west = west

        # connect adjacent rooms to each other. for example, if the northern room of room1 is room2, then the
        # southern room of room2 will be room1.
        if north:
            north.south = self
        if east:
            east.west = self
        if south:
            south.north = self
        if west:
            west.east = self

    def describe_room(self) -> None:
        """Display the name of the place to the player. If the player has not visited the room before, describe it.
        If there are any items in the room, list their names to the player.
        """
        print(f'{self.name}')

        if not self.visited:
            print(f'{self.description} \n')
            self.visited = True
        else:
            print('')


################################################################
# PLAYER
################################################################


class Player:
    """Class representing the player character.

    location: The current location of the player.
    inventory: A list of items that the player is holding.
    """
    location: Room
    inventory: set[Item]

    def __init__(self, location: Room) -> None:
        """Initialise a new Player instance."""
        self.location = location
        self.inventory = set()

    def open_inventory(self) -> None:
        """Print out a list of items in the player's inventory."""
        print('You have:')
        for item in self.inventory:
            print(f'    {item.name}')

    def pickup_item(self, item: Item, container: Container) -> None:
        """Remove an item from a container in the player's location and put it into the player's inventory.
        If the given item is not in the player's location, then inform the player and do nothing.
        """
        if not item.portable:
            print('You can\'t pick that up!')
        elif container is self.location or (container in self.location.contents and not container.locked):
            container.contents.remove(item)
        else:
            print('Either it\'s not in the room, or I can\'t understand you.')
            return None

        self.inventory.add(item)

    def unlock_container(self, key: Item, container: Container) -> None:
        """Attempt to unlock a container with a key in the players inventory. If the key is in the player's inventory,
        attempt to unlock the container. If it isn't, tell the player and do nothing.
        """
        if key in self.inventory:
            container.unlock_container(key)
            for item in container.contents:
                self.location.contents.add(item)
        else:
            print('You don\'t have that key!')

    def move(self, direction: str) -> None:
        """Move into a new room: when called, update the location of the player and describe the room."""
        # find room in direction
        if direction == 'north' or direction == 'n':
            room = self.location.north
        elif direction == 'east' or direction == 'e':
            room = self.location.east
        elif direction == 'south' or direction == 's':
            room = self.location.south
        elif direction == 'west' or direction == 'w':
            room = self.location.west
        else:
            print('I don\'t know what direction that is.')
            return None

        if room is None:
            print('You can\'t go that way.')
            return None
        # TODO: implementation for locked rooms feature
        # elif room.locked:
        #   ...
        else:
            self.location = room

        self.location.describe_room()

    def take_item(self, item_name: str) -> None:
        """Given the name of an item, search for the item in the player's location. If the item is found,
        place it into the player's inventory. If not, then tell the player and do nothing.
        """
        for item in self.location.contents:
            if item_name in item.keywords and item.portable:
                self.inventory.add(item)
                print(f'Took {item.name.lower()}.')
                return None
            elif item_name in item.keywords and not item.portable:
                print('You can\'t take that!')
                return None

        print('I can\'t find that item.')

    def inspect_item(self, item_name: str) -> None:
        """Given the name of an item, search for the item in the player's location. If the item is found,
        print the description of the item. If not, then tell the player and do nothing.
        """
        if item_name == self.location.name or item_name == 'room':
            print(self.location.description)
            return None

        for item in set.union(self.location.contents, self.inventory):
            if item_name in item.keywords:
                print(item.description)
                return None

        print('I can\'t find that item.')


################################################################
# TOP-LEVEL FUNCTIONS
################################################################
