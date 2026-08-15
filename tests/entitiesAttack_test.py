import unittest
from entities import Human, Dwarf, Elf, Orc, Troll
from constAndEnum import Kinds

class TestAttackEntity(unittest.TestCase):
    def test_attack_correct(self):
        ent1 = Human('Greg')
        ent2 = Elf('Twinkle')
        print('Attack: happy path')
        ent1.attack(ent2)
        list1 = [ent2.kind, 
                ent2.health,
                ent2.dmg, 
                ent2.arm, 
                ent2.dmgres,
                ent2.name
                ]
        list2 = [Kinds.ELF,
                 109,
                 8, 
                 4, 
                 2,
                 'Twinkle'
                 ]
        print(list1, list2)
        self.assertEqual(list1, list2)

    def test_attack_dmg_less_than_arm(self):
        ent1 = Elf('Twinkle')
        ent2 = Troll()
        print('Attack: dmg lower than arm')
        ent1.attack(ent2)
        list1 = [ent2.kind, 
                ent2.health,
                ent2.dmg, 
                ent2.arm, 
                ent2.dmgres,
                ent2.name
                ]
        list2 = [Kinds.TROLL,
                 350,
                 22,
                 10,
                 15,
                 None
                 ]
        print(list1, list2)
        self.assertEqual(list1, list2)

if __name__ == '__main__':
    unittest.main()