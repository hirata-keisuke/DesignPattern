from src.mapsite import SimpleDoor, SimpleRoom
import unittest

class SimpleMazeTest(unittest.TestCase):

    def test_door_effect(self):
        door = SimpleDoor(None, None)
        other = door.clone()
        
        self.assertEqual("ただのドアです。", door.effect())

    def test_door_clone(self):
        import copy
        r1 = SimpleRoom(1)
        door = SimpleDoor(r1, copy.deepcopy(r1))
        other = copy.deepcopy(door)
        
        self.assertIsNot(other, door)
        self.assertIsNot(r1, door._room1)

    def test_room(self):
        room = SimpleRoom(1)
        other = room.clone()

        self.assertEqual("ただの部屋です。", room.effect())
        self.assertIsNot(other, room)

if __name__ == "__main__":
    unittest.main()