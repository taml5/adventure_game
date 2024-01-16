"""Interprets player input into valid input data for the GameInteractor."""
from engine.gameinteractor import GameInteractor


class Controller:
    """Interprets player input into valid input data for the GameInteractor.

    interactor: the game interactor.
    """
    interactor: GameInteractor
    item_ids: dict[str: int]

    def __int__(self, interactor: GameInteractor, item_ids: dict[str: int]):
        self.interactor = interactor
        self.item_ids = item_ids

    def item_id(self, item_name: str) -> int:
        """Given the name of an item, return its item_id.

        Precondition:
        - item_name is a valid name of an existing item.
        """
        item_name = item_name.strip().lower()
        return self.item_ids.get(item_name)
