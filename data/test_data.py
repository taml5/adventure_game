"""This module contains some test items and rooms that can be used to test the game."""

from entities.room import Room
from entities.item import Item, Container

################################################################
# ITEMS
################################################################

# test_room1
test_key = Item(item_id=hash('Key1'))
test_key.set_attributes(name='Rusty Key',
                        description='The key is old and rusted.',
                        portable=True,
                        interactable=True
                        )
test_item1 = Item(item_id=hash('Sword'))
test_item1.set_attributes(name='Sword',
                          description='A one-handed sword made of bronze, forged in a bygone era by an ancient '
                                      'civilisation. It\'s still sharp.',
                          portable=True,
                          interactable=True
                          )
test_chest = Container(hash('chest1'))
test_chest.set_attributes(name='Old Chest',
                          description='The chest is ancient: the wood is rotted and covered in moss. '
                                      'Yet, the lock still holds firm.',
                          portable=False,
                          interactable=True
                          )
test_chest.container_attributes(locked=True,
                                key=test_key,
                                contents={test_item1})

# test_room2
test_item2 = Item(hash('pendant1'))
test_item2.set_attributes(name='Ruby Pendant',
                          description='A pendant of gold with a large ruby inlaid in the middle. The gold is dull, '
                                      'but the ruby still shines brightly despite the dim light in the room.',
                          portable=True,
                          interactable=True
                          )

################################################################
# ROOMS
################################################################

test_room1 = Room()
test_room1.name = 'Test Room'
test_room1.description = 'This is a test room. There is a rusty key and a chest.',
test_room1.add_item(test_key)
test_room1.add_item(test_chest)

test_room2 = Room()
test_room2.name = 'Secret Room'
test_room2.description = 'This is another room connected to the main room. There is a pendant lying on the floor.'
test_room2.add_item(test_item2)
test_room2.add_neighbour(test_room1, 'south')
