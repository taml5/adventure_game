"""This module contains the Room class, Item class, and Player class, as well as their respective methods."""

from typing import Optional

DIRECTIONS = {'n', 'e', 's', 'w', 'north', 'east', 'south', 'west'}
COMMANDS = {'quit': {'quit', 'q'},
            'move': {'move', 'go', 'walk'}.union(DIRECTIONS),  # shortcuts for directions work as move command
            'inventory': {'inventory', 'i'},
            'take': {'take', 'grab', 'get'},
            'interact': {'use'},
            'unlock': {'unlock', 'open'},
            'inspect': {'inspect', 'examine', 'describe'},
            'help': {'help', 'h'}
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

    def display_contents(self) -> str:
        """Print the contents of the container to the player. If there is nothing inside the container,
        tell the player.
        """
        if not self.contents:
            return f'It is empty.'

        contents_str = f'The {self.name.lower()} contains: \n'
        for item in self.contents:
            if isinstance(item, Container):
                contents_str += f'{item.name} \n'
                contents_str += item.display_contents() + '\n'
            else:
                contents_str += f'{item.name} \n'

        return contents_str

    def unlock_container(self, key: Item) -> str:
        """Attempt to unlock the container with the given item. If it is already unlocked, tell the player. If the
        key is correct, unlock the container. Else, tell the player the key doesn't work.
        """
        if not self.locked:
            return 'It doesn\'t seem to be locked.'
        elif key.name == self.key.name:
            self.locked = False
            print(f'The {self.name.lower()} unlocks. \n')
            return self.display_contents()
        else:
            return f'The key doesn\'t seem to fit.'

    def search_for_item(self, item_name: str) -> tuple[Item, 'Container'] | None:
        """Given the name of an item, search for the item within this container. If it is found, return
        a tuple containing the item and the direct container containing it."""
        for item in self.contents:
            if item_name in item.keywords:
                return (item, self)
            elif isinstance(item, Container) and item.locked is False:
                return item.search_for_item(item_name)

        # if the item can't be found inside the container
        return None

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

    def __init__(self, name: str, description: str, contents: set[Item | Container], locked: bool,
                 key: Optional[Item] = None, north: Optional['Room'] = None, east: Optional['Room'] = None,
                 south: Optional['Room'] = None, west: Optional['Room'] = None) -> None:
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
    inventory: Container

    def __init__(self, location: Room) -> None:
        """Initialise a new Player instance."""
        self.location = location
        self.inventory = Container(name='inventory',
                                   keywords={'inventory'},
                                   description='The inventory of the player',
                                   interactable=False,
                                   portable=True,
                                   contents=set(),
                                   locked=False,)

    def find_item(self, item_name: str) -> tuple[Item, Container] | None:
        """Search for an item in the contents of the player's location. If found, return a tuple containing
        the item and the direct container it is in. Otherwise, return None."""
        # search for item in inventory
        inventory_search = self.inventory.search_for_item(item_name)
        if inventory_search is not None:
            return inventory_search
        # search for item in location
        location_search = self.location.search_for_item(item_name)
        if location_search is not None:
            return location_search

        # item not in location or inventory
        return None

    def open_inventory(self) -> None:
        """Print out a list of items in the player's inventory."""
        print('You have:')
        for item in self.inventory.contents:
            print(f'    {item.name}')

    def unlock_with_key(self, key_name: str, item_name: str) -> str:
        """Attempt to unlock an Item with a key in the players inventory. If the key is in the player's inventory,
        attempt to unlock the container. If it isn't, tell the player and do nothing.
        """
        # check if key is in the room
        key = self.find_item(key_name)
        if key is None:
            return 'You don\'t have that key!'

        find_item = self.find_item(item_name)
        if find_item is not None:
            item = find_item[0]
            if isinstance(item, Container):
                return item.unlock_container(key[0])
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
            return

        if room is None:
            print('You can\'t go that way.')
        elif room.locked:
            print('That way is locked.')
        else:
            self.location = room
            print(self.location.describe_room())

    def take_item(self, item_name: str) -> str:
        """Given the name of an item, search for the item in the player's location. If the item is found,
        place it into the player's inventory. If not, then tell the player and do nothing.
        """
        find_item = self.find_item(item_name)

        if find_item is None:
            return 'I can\'t find that.'
        elif find_item[1] is self.inventory:
            return 'You already took that.'
        elif not find_item[0].portable:
            return 'You can\'t take that!'
        else:
            item, container = find_item
            self.inventory.contents.add(item)
            container.contents.remove(item)
            return f'Took {item.name.lower()}.'

    def inspect_item(self, item_name: str) -> str:
        """Given the name of an item, search for the item in the player's location. If the item is found,
        print the description of the item. If not, then tell the player and do nothing.
        """
        if item_name.lower() in self.location.name.lower() or item_name == 'room':
            return self.location.description
        else:
            find_item = self.find_item(item_name)
            if find_item is None:
                return 'I can\'t find that item.'

            item = find_item[0]
            if isinstance(item, Container) and item.locked is False:
                string = f"""{item.description}\n\n{item.display_contents()}"""
                return string
            else:
                return item.description

################################################################
# TOP-LEVEL FUNCTIONS
################################################################

def game_quit(player: Player) -> bool:
    """Ask the player if they want to quit or not. If they confirm they want to quit, end the game."""
    while True:
        print('Are you sure you want to quit?')
        user_input = input('> ').lower().strip()

        if user_input == 'yes' or user_input == 'y':
            print('Ending the game... \n')
            return False
        elif user_input == 'no' or user_input == 'n':
            print(player.location.describe_room())
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
