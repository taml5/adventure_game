"""Defines the item entity and its subclasses."""


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

    def __init__(self, item_id: int):
        self.item_id = item_id
        self.name = ''
        self.description = ''
        self.interactable = False
        self.portable = False


class Container(Item):
    """An item that can contain other items.

    contents: items that the Container contains, represented as a dictionary mapping from item_id to the Item.
    """
    contents: dict[int: Item]

    def __init__(self, item_id: int):
        super().__init__(item_id)
        self._contents = {}
