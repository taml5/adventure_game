"""TODO: write module docstring"""


class Item:
    """TODO: write docstring"""
    item_id: int
    name: str
    description: str
    _interactable: bool
    _portable: bool

    def __init__(self, item_id: int):
        self.item_id = item_id
        self.name = ''
        self.description = ''
        self.interactable = False
        self.portable = False


class Container(Item):
    """TODO: write docstring"""
    contents: dict[int: Item]

    def __init__(self, item_id: int):
        super().__init__(item_id)
        self._contents = {}
