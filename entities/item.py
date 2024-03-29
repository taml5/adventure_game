"""Defines the item entity and its subclasses."""
from typing import Iterable


class Item:
    """An item in the game.

    item_id: the id of the item which the engine uses to keep track of the item.
    name: the name of the item.
    description: a description of the item.
    portable: if the player can pick the item up or not.
    events: a collection of events associated with this item that can occur.
    """
    item_id: int
    name: str
    description: str
    portable: bool

    def __init__(self, item_id: int, name: str, description: str, interactable: bool, portable: bool):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.interactable = interactable
        self.portable = portable


class Container(Item):
    """An item that can contain other items.

    contents: items that the Container contains, represented as a dictionary mapping from item_id to the Item.
    locked: whether the Container is locked or not.
    key: the corresponding key if the Container is locked; otherwise None.
    """
    contents: dict[int: Item]
    locked: bool

    def __init__(self, item_id: int,
                 name: str,
                 description: str,
                 interactable: bool,
                 locked: bool):
        super().__init__(item_id, name, description, interactable, False)
        self.contents = {}
        self.locked = locked

    def insert_item(self, item: Item) -> None:
        """Insert the given item into the Container."""
        self.contents[item.item_id] = item

    def insert_items(self, items: Iterable[Item]) -> None:
        """Insert the given items into the Container."""
        for item in items:
            self.insert_item(item)
