from src.mapsite import BombedRoom
import unittest

class SimpleMazeTest(unittest.TestCase):

    def test_room(self):
        room = BombedRoom(1)
        other = room.clone()

        self.assertEqual("ドッカーン！！！", room.effect())
        self.assertIsNot(other, room)

if __name__ == "__main__":
    unittest.main()