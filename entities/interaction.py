"""Defines the abstract class Interaction.

An interaction occurs between a specific item and the environment. When the player attempts to use the
item in the correct room and all conditions are met, a script is run which modifies the game environment,
and a message is returned that informs the player of what happened.

TODO: figure out interactions and how to execute them
"""
from typing import Callable
from abc import ABC, abstractmethod

from entities.item import Item


class Interaction(ABC):
    """An abstract class that represents an arbitrary interaction between the player,
    the item, and the environment.

    key_item: the item that is used in order to initiate this interaction.
    interaction: a function that defines the interaction.
    """
    key_item: Item
    interaction: Callable

    def __int__(self, item1: Item, interaction: Callable):
        self.key_item = item1
        self.interaction = interaction

    def __contains__(self, item):
        # use is since there should be no duplicates of items
        return self.key_item is item

    @abstractmethod
    def execute_interaction(self):
        """Execute the interaction."""
        raise NotImplementedError
