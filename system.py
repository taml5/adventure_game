"""This module contains the Room class, Item class, and Player class, as well as their respective methods."""

from typing import Optional

DIRECTIONS = {'n', 'e', 's', 'w', 'north', 'east', 'south', 'west'}
COMMANDS = {'quit': {'quit', 'q'},
            'move': {'move', 'go', 'walk'}.union(DIRECTIONS),  # shortcuts for directions work as move command
            'inventory': {'inventory', 'i'},
            'take': {'take', 'grab'},
            'interact': {'use'},
            'unlock': {'unlock'},
            'inspect': {'inspect', 'examine'},
            'help': {'help'}
            }

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

    def unlock_container(self, key: Item) -> str:
        """Attempt to unlock the container with the given item. If it is already unlocked, tell the player. If the
        key is correct, unlock the container. Else, tell the player the key doesn't work.
        """
        if not self.locked:
            return 'It doesn\'t seem to be locked.'
        elif key.name == self.key.name:
            self.locked = False
            print(f'The {self.name.lower()} unlocks. \n')
            self.display_contents()
            return ''
        else:
            return f'The key doesn\'t seem to fit.'


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

    def __init__(self, name: str, description: str, contents: set[Item], locked: bool, key: Optional[Item] = None,
                 north: Optional['Room'] = None, east: Optional['Room'] = None, south: Optional['Room'] = None,
                 west: Optional['Room'] = None) -> None:
        """Initialise a new Room instance."""
        self.visited = False
        Container.__init__(self, name=name, keywords=set(), description=description, interactable=False,
                           portable=False, contents=contents, locked=locked, key=key)
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

    def describe_room(self) -> str:
        """Display the name of the place to the player. If the player has not visited the room before, describe it.
        If there are any items in the room, list their names to the player.
        """
        print(f'{self.name}')

        if not self.visited:
            self.visited = True
            return f'{self.description} \n'
        else:
            return ''


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

    def find_item(self, item_name: str) -> Item | None:
        """Search for an item in the contents of the player's location. If found, return it.
        Else, return an empty item."""
        for item in self.location.contents:
            if item_name in item.keywords:
                return item

        return None

    def open_inventory(self) -> None:
        """Print out a list of items in the player's inventory."""
        print('You have:')
        for item in self.inventory:
            print(f'    {item.name}')

    def unlock_with_key(self, key: Item, container: Container) -> str:
        """Attempt to unlock a container with a key in the players inventory. If the key is in the player's inventory,
        attempt to unlock the container. If it isn't, tell the player and do nothing.
        """
        if key in self.inventory:
            self.location.contents = self.location.contents.union(container.contents)
            return container.unlock_container(key)
        else:
            return 'You don\'t have that key!'

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
        elif room.locked:
            print('That way is locked.')
            return None
        else:
            self.location = room

        self.location.describe_room()

    def take_item(self, item_name: str) -> str:
        """Given the name of an item, search for the item in the player's location. If the item is found,
        place it into the player's inventory. If not, then tell the player and do nothing.
        """
        item = self.find_item(item_name)
        if item is None:
            return 'I can\'t find that item.'
        elif item in self.inventory:
            return 'You already have that.'
        elif not item.portable:
            return 'You can\'t take that!'
        else:
            self.inventory.add(item)
            return f'Took {item.name.lower()}.'

    def inspect_item(self, item_name: str) -> str:
        """Given the name of an item, search for the item in the player's location. If the item is found,
        print the description of the item. If not, then tell the player and do nothing.
        """
        if item_name in self.location.name.lower() or item_name == 'room':
            return self.location.description

        item = self.find_item(item_name)
        if item is None:
            return 'I can\'t find that item.'
        else:
            return item.description


################################################################
# TOP-LEVEL FUNCTIONS
################################################################

def game_quit() -> bool:
    """Ask the player if they want to quit or not. If they confirm they want to quit, end the game."""
    while True:
        print('Are you sure you want to quit?')
        user_input = input('> ').lower().strip()

        if user_input == 'yes' or user_input == 'y':
            print('Ending the game... \n')
            return False
        elif user_input == 'no' or user_input == 'n':
            return True
        else:
            print('I don\'t understand.')


def game_help() -> None:
    """Provide a list of commands that the player can use and direct them on how to interact with the game."""
    print('To play the game, input a command into the console: for example, "go north" or "inspect room".')
    print('Available commands:')
    for command in COMMANDS:
        print(f'    {command}')
    print('')
