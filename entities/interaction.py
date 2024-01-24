"""Defines the abstract class Interaction.

An interaction occurs between a specific item and the environment. When the player attempts to use the
item in the correct room and all conditions are met, a script is run which modifies the game environment,
and a message is returned that informs the player of what happened.

TODO: figure out interactions and how to execute them
"""
from abc import ABC, abstractmethod

from entities.item import Item


class Interaction(ABC):
    """An abstract class that represents an arbitrary interaction between the player,
    the item, and the environment.

    item1: the item that is used in order to initiate this interaction.
    """
    item1: Item

    def __int__(self, item1: Item):
        self.item1 = item1

    def __contains__(self, item):
        return self.item1 is item

    @abstractmethod
    def execute_interaction(self) -> str:
        """Execute the interaction by modifying the game environment and return a
        message describing the interaction that took place.
        """
        raise NotImplementedError
