"""This module contains some test items and rooms that can be used to test the game."""

from entities.room import Room
from entities.item import Item, Container

################################################################
# ITEMS
################################################################

# test_room1
TEST_KEY = Item(name='Rusty Key',
                item_id=hash('Key1'),
                description='The key is old and rusted.',
                portable=True,
                interactable=True,
                )
TEST_ITEM1 = Item(name='Sword',
                  item_id=hash('Sword'),
                  description='A one-handed sword made of bronze, forged in a bygone era by an ancient '
                              'civilisation. It\'s still sharp.',
                  portable=True,
                  interactable=True
                  )
TEST_CHEST = Container(name='Old Chest',
                       item_id=hash('chest1'),
                       description='The chest is ancient: the wood is rotted and covered in moss. '
                                   'Yet, the lock still holds firm.',
                       interactable=True,
                       locked=True
                       )
TEST_CHEST.insert_item(TEST_ITEM1)

# test_room2
TEST_ITEM2 = Item(name='Ruby Pendant',
                  item_id=hash('Ruby Pendant'),
                  description='A pendant of gold with a large ruby inlaid in the middle. The gold is dull, '
                              'but the ruby still shines brightly despite the dim light in the room.',
                  portable=True,
                  interactable=True
                  )

################################################################
# ROOMS
################################################################

TEST_ROOM1 = Room(name='Test Room',
                  description='This is a test room. There is a rusty key and a chest.',)
TEST_ROOM1.add_item(TEST_KEY)
TEST_ROOM1.add_item(TEST_CHEST)

TEST_ROOM2 = Room(name='Secret Room',
                  description='This is another room connected to the main room. There is a pendant lying on the floor.')
TEST_ROOM2.add_item(TEST_ITEM2)
TEST_ROOM2.add_neighbour(TEST_ROOM1, 'south')
