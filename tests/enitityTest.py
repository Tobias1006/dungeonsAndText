import unittest
from entities import Human, Dwarf, Elf, Orc, Troll
from constAndEnum import Kinds

class TestParentNode(unittest.TestCase):
    def test_create_human(self):
        human1 = Human('Greg')
        print('Create Human: Greg')
        list1 = [human1.kind, 
                 human1.health,
                 human1.dmg, 
                 human1.spd,
                 human1.arm, 
                 human1.dmgres,
                 human1.name
                 ]
        list2 = [Kinds.HUMAN,
                 100,
                 30,
                 10,
                 3,
                 0,
                 'Greg'
                 ]
        self.assertEqual(list1, list2)

if __name__ == '__main__':
    unittest.main()
