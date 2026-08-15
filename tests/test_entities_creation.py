import unittest
from entities import Human, Dwarf, Elf, Orc, Troll
from const_and_enum import Kinds

class TestCreateEntity(unittest.TestCase):
    def test_create_default_human(self):
        ent1 = Human()
        print('Create Human: generic')        
        self.assertEqual(ent1.kind, Kinds.HUMAN)
        self.assertEqual(ent1.health, 10)
        self.assertEqual(ent1.dmg, 4)
        self.assertEqual(ent1.arm, 3)
        self.assertEqual(ent1.dmgres, 0)
        self.assertEqual(ent1.name, 'Steven')
    
    def test_create_default_elf(self):
        ent1 = Elf()
        print('Create Elf: generic')        
        self.assertEqual(ent1.kind, Kinds.ELF)
        self.assertEqual(ent1.health, 12)
        self.assertEqual(ent1.dmg, 3)
        self.assertEqual(ent1.arm, 3)
        self.assertEqual(ent1.dmgres, 2)
        self.assertEqual(ent1.name, 'Twinkle')

    def test_create_default_dwarf(self):
        ent1 = Dwarf()
        print('Create Dwarf: generic')
        self.assertEqual(ent1.kind, Kinds.DWARF)
        self.assertEqual(ent1.health, 13)
        self.assertEqual(ent1.dmg, 5)
        self.assertEqual(ent1.arm, 5)
        self.assertEqual(ent1.dmgres, 0)
        self.assertEqual(ent1.name, 'Grobnob')

    def test_create_default_orc(self):
        ent1 = Orc()
        print('Create Orc: generic')
        self.assertEqual(ent1.kind, Kinds.ORC)
        self.assertEqual(ent1.health, 8)
        self.assertEqual(ent1.dmg, 4)
        self.assertEqual(ent1.arm, 3)
        self.assertEqual(ent1.dmgres, 0)
        self.assertEqual(ent1.name, 'Krsprk')

    def test_create_default_troll(self):
        ent1 = Troll()
        print('Create Troll: generic')
        self.assertEqual(ent1.kind, Kinds.TROLL)
        self.assertEqual(ent1.health, 35)
        self.assertEqual(ent1.dmg, 22)
        self.assertEqual(ent1.arm, 10)
        self.assertEqual(ent1.dmgres, 15)
        self.assertEqual(ent1.name, 'Dum-Dum')

    def test_create_entities_custom_name(self):
        ent1 = Human('Greg')
        ent2 = Elf('Elfrong')
        ent3 = Dwarf('Dunadin')
        ent4 = Orc('Frgsprt')
        ent5 = Troll('Num-Num')
        print('Check custom name')
        self.assertEqual(ent1.name, 'Greg')
        self.assertEqual(ent2.name, 'Elfrong')
        self.assertEqual(ent3.name, 'Dunadin')
        self.assertEqual(ent4.name, 'Frgsprt')
        self.assertEqual(ent5.name, 'Num-Num')    

    def test_create_entities_default_is_alive_true(self):
        ent1 = Human()
        ent2 = Elf()
        ent3 = Dwarf()
        ent4 = Orc()
        ent5 = Troll()
        print('Check intital is_alive for all entities = true')
        self.assertEqual(ent1.is_alive, True)
        self.assertEqual(ent2.is_alive, True)
        self.assertEqual(ent3.is_alive, True)
        self.assertEqual(ent4.is_alive, True)
        self.assertEqual(ent5.is_alive, True)

if __name__ == '__main__':
    unittest.main()
