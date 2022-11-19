from src.mapsite import SimpleDoor
import unittest

class SimpleMazeTest(unittest.TestCase):

    def test_door_effect(self):
        door = SimpleDoor(1, 2)
        other = door.clone()
        
        self.assertEqual("ただのドアです。", door.effect())

    def test_door_clone(self):
        door = SimpleDoor(1, 2)
        other = door.clone()
        
        self.assertIsNot(other, door)

if __name__ == "__main__":
    unittest.main()