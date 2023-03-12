"""This module contains some test items and rooms that can be used to test the game."""

from system import Item, Room, Container

################################################################
# ITEMS
################################################################

# test_room1
test_key = Item(name='Rusty Key',
                description='The key is old and rusted.',
                keywords={'key', 'rusty key'},
                portable=True,
                interactable=True
                )
test_item1 = Item(name='Sword',
                  description='A one-handed sword made of bronze, forged in a bygone era by an ancient '
                              'civilisation. It\'s still sharp.',
                  keywords={'sword'},
                  portable=True,
                  interactable=True
                  )
test_chest = Container(name='Old Chest',
                       description='The chest is ancient: the wood is rotted and covered in moss. '
                                   'Yet, the lock still holds firm.',
                       locked=True,
                       key=test_key,
                       contents={test_item1},
                       keywords={'chest', 'container'},
                       portable=False,
                       interactable=True
                       )
# test_room2
test_item2 = Item(name='Ruby Pendant',
                  description='A pendant of gold with a large ruby inlaid in the middle. The gold is dull, '
                              'but the ruby still shines brightly despite the dim light in the room.',
                  keywords={'pendant', 'ruby pendant', 'gold pendant'},
                  portable=True,
                  interactable=True
                  )

################################################################
# ROOMS
################################################################

test_room1 = Room(name='Test Room',
                  description='This is a test room. There is a rusty key and a chest.',
                  contents={test_key, test_chest},
                  locked=False
                  )
test_room2 = Room(name='Secret Room',
                  description='This is another room connected to the main room. '
                              'There is a pendant lying on the floor.',
                  contents={test_item2},
                  south=test_room1,
                  locked=False
                  )
