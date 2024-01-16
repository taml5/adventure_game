"""Defines the valid input data for GameInteractor"""
from dataclasses import dataclass


@dataclass
class InteractorData:
    """Defines the valid input data for GameInteractor"""
    command: str
    item_ids: list[int]
    direction: str

    def __int__(self, command: str, item_ids: list[int], direction: str):
        self.command = command
        self.item_ids = item_ids
        self.direction = direction
