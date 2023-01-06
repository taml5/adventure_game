"""This is the main module that runs the game."""
import system
from data import test_data

# from data import rooms
# from data import items

player = system.Player(location=test_data.test_room1)


# TODO: implement commands that the player can input
DIRECTIONS = {'n', 'e', 's', 'w', 'north', 'east', 'south', 'west'}
COMMANDS = {'quit': {'quit', 'q'},
            'move': {'move', 'go', 'walk'}.union(DIRECTIONS),
            'inventory': {'inventory', 'i'},
            'take': {'take', 'grab'},
            'interact': {'use'},
            'unlock': {'unlock'},
            'inspect': {'inspect', 'examine'},
            'help': {'help'}
            }


def game_loop() -> bool:
    """The main game loop. Given an input by the player, respond to the input according to what command was given.
    """
    user_input = input('> ').lower().split(' ')

    # TODO: implement function for processing input before response

    # respond to user input
    if user_input[0] in COMMANDS['quit']:
        print('Ending the game... \n')
        return False
    elif user_input[0] in COMMANDS['inventory']:
        player.open_inventory()
    elif user_input[0] in COMMANDS['move']:
        if len(user_input) != 1:
            direction = user_input[1]
        elif user_input[0] in DIRECTIONS:
            direction = user_input[0]
        else:
            print('Move where?')
            direction = input('> ')

        player.move(direction)
    elif user_input[0] in COMMANDS['take']:
        # TODO: implement solution for taking items from container in room instead just items in the room
        item_name = user_input[1]
        player.take_item(item_name)
    elif user_input[0] in COMMANDS['interact']:
        # TODO: implement solution for interacting with items
        ...
        raise NotImplementedError
    elif user_input[0] in COMMANDS['unlock']:
        # TODO: implement solution for unlocking containers
        ...
        raise NotImplementedError
    elif user_input[0] in COMMANDS['inspect']:
        # TODO: implement solution for examining rooms and items
        ...
        item_name = user_input[1]
        player.inspect_item(item_name)
    elif user_input[0] in COMMANDS['help']:
        # TODO: implement solution for helping player
        ...
        raise NotImplementedError
    else:
        print("I don't understand.")

    return True


if __name__ == '__main__':
    player.location.describe_room()
    while game_loop():
        pass
