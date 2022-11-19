from src.mapsite import SimpleDoor
import unittest

class SimpleMazeTest(unittest.TestCase):

    def test_door(self):
        door = SimpleDoor(1, 2)
        
        self.assertEqual("ただのドアです。", door.effect())


if __name__ == "__main__":
    unittest.main()