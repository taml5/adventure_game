"""The engine of the adventure game.

This contains the GameInteractor that contains the needed logic to manipulate entities, and output the relevant data
to the Presenter to be shown to the player.
"""
from entities.player import Player
from entities.item import Item, Container


class GameInteractor:
    """TODO: write docstring

    TODO: change all command methods to return a list of strings instead
    """
    player: Player

    def __init__(self, player: Player) -> None:
        self.player = player

    def get_help(self) -> list[str]:
        """Return the help command.

        TODO: write a better help response
        """
        return ["Good luck!"]

    def open_inventory(self) -> list[str]:
        """Return a list of the item names that are in the player's inventory. If it is empty, return a message
        informing the player that they are holding no items.
        """
        if len(self.player.inventory) == 0:
            return ["You aren't carrying anything."]
        else:
            output = []
            for item in self.player.inventory.values():
                output.append(item.name)
            return output

    def describe_room(self) -> list[str]:
        """Return the description of the room."""
        return [self.player.location.description]

    def announce_room(self) -> list[str]:
        """Return the name of the room. If it is the first time visiting this room, return the description
        of the room as well.
        """
        if self.player.location.visited:
            return [self.player.location.name]
        else:
            self.player.location.visited = True
            return [self.player.location.name, self.player.location.description]

    def move_rooms(self, direction: str) -> list[str]:
        """Attempt to move the player into a neighbouring room."""
        neighbouring_rooms = self.player.location.neighbours
        if direction in neighbouring_rooms:
            self.player.location = neighbouring_rooms[direction]
            if not self.player.location.visited:
                return self.announce_room()
            else:
                return [self.player.location.name]
        else:
            return ["You can't move that way!"]

    def pickup_item(self, item_id: int) -> list[str]:
        """Pick an item up from the player's location and place it in the player's inventory.
        """
        item, in_inventory = self.find_item(item_id)
        if item is None:  # item not found
            return ["I can't find that item."]
        elif in_inventory:  # item is already in the inventory
            return ["You already have that."]
        elif not item[0].portable:  # cannot pick up that item
            return ["You can't pick that up."]
        else:
            item = self.player.location.pop_item(item_id)
            if isinstance(item, Container):  # different behaviour if item is a Container
                output = []
                for subitem in item.contents:
                    output.extend(self.pickup_item(subitem.item_id))
                return output
            else:
                self.player.add_item(item)
                return [f"Picked up {item.name}."]

    def drop_item(self, item_id: int) -> list[str]:
        """Attempt to drop an item from the player's inventory. If the player does not have it, do nothing and
        inform the player.
        """
        if self.player.has_item(item_id):
            item = self.player.inventory[item_id]
            self.player.drop_item(item)
            return [f"Dropped {item.name}."]
        else:
            return [f"You don't have that."]

    def handle_invalid_event(self) -> list[str]:
        """Return a string informing the player that they have entered an invalid command."""
        return ["I don't know you're trying to say."]

    def find_item(self, item_id: int) -> tuple[Item, bool] | tuple[None, None]:
        """Find the given item in the player's vicinity (location or inventory). If found, return the item and
        if it is in the player's inventory as a tuple. Otherwise, return None."""
        if self.player.has_item(item_id):
            return (self.player.inventory[item_id], True)
        elif self.player.location.contains(item_id):
            return (self.player.location.contents[item_id], False)
        else:
            return None, None
