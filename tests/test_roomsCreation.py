import unittest
from entities import Human, Dwarf, Elf, Orc, Troll
from rooms import Hallway, Story, Fight, End
from constAndEnum import Rooms
from constAndEnum import Kinds

class TestCreateRoom(unittest.TestCase):
    def test_create_room_hallway(self):
        l_o_r = [1,2,3,4]
        room1 = Hallway(l_o_r)
        print('Create Room: Hallway | l_o_r = [1,2,3,4]')
        list1 = [room1.kind,
                 room1.adj_rooms,
                 room1.entity,
                 room1.story,
                 room1.already_visited
                 ]
        list2 = [Rooms.HALLWAY,
                 [1,2,3,4],
                 None,
                 None,
                 False
                 ]
        self.assertEqual(list1, list2)
        
    def test_create_room_story(self):
        l_o_r = [1,2,3,4]
        story = 1
        room1 = Story(l_o_r, story)
        print('Create Room: Story | l_o_r = [1,2,3,4], story = 1')
        list1 = [room1.kind,
                 room1.adj_rooms,
                 room1.entity,
                 room1.story,
                 room1.already_visited
                 ]
        list2 = [Rooms.STORY,
                 [1,2,3,4],
                 None,
                 1,
                 False
                 ]
        self.assertEqual(list1, list2)
            
    def test_create_room_fight(self):
        l_o_r = [1,2,3,4]
        entity = Orc()
        room1 = Fight(l_o_r, entity)
        print('Create Room: Story | l_o_r = [1,2,3,4], entity = Orc')
        list1 = [room1.kind,
                 room1.adj_rooms,
                 room1.entity.kind,
                 room1.story,
                 room1.already_visited
                 ]
        list2 = [Rooms.FIGHT,
                 [1,2,3,4],
                 Kinds.ORC,
                 None,
                 False
                 ]
        self.assertEqual(list1, list2)


if __name__ == '__main__':
    unittest.main()
