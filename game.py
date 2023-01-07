"""This is the main module that runs the game."""
import system
from system import DIRECTIONS, COMMANDS
from data import test_data

# from data import rooms
# from data import items

player = system.Player(location=test_data.test_room1)


def game_loop() -> bool:
    """The main game loop. Given an input by the player, respond to the input according to what command was given.
    """
    user_input = input('> ').lower().split(' ')

    # TODO: implement function for processing input before response

    # respond to user input
    if user_input[0] in COMMANDS['quit']:
        return system.quit_game()
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
        item_name = user_input[1]
        print(player.take_item(item_name))
    elif user_input[0] in COMMANDS['interact']:
        # TODO: implement solution for interacting with items
        ...
        raise NotImplementedError
    elif user_input[0] in COMMANDS['unlock']:
        # TODO: implement solution for unlocking containers
        ...
        raise NotImplementedError
    elif user_input[0] in COMMANDS['inspect']:
        item_name = user_input[1]
        print(player.inspect_item(item_name))
    elif user_input[0] in COMMANDS['help']:
        system.game_help()
    else:
        print("I don't understand.")

    return True


if __name__ == '__main__':
    player.location.describe_room()
    while game_loop():
        pass
