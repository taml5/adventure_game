"""TODO: write module docstring"""


class Item:
    """TODO: write docstring"""
    id: int
    name: str
    description: str
    _interactable: bool
    _portable: bool

    def __init__(self, id: int):
        self.id = id
        self.name = ''
        self.description = ''
        self.interactable = False
        self.portable = False


class Container(Item):
    """TODO: write docstring"""
    contents: dict[int: Item]

    def __init__(self, id: int):
        super().__init__(id)
        self._contents = {}
