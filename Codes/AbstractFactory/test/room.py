import unittest
from src.room import Room
from src.wall import Wall

class RoomTest(unittest.TestCase):

    def test_room_attributes(self):
        """迷路を構成する部屋が想定している属性を持つことを確認する
        """

        room = Room(room_number=1)

        self.assertEqual(1, room.number)
        self.assertIsNone(room.west)
        self.assertIsNone(room.east)
        self.assertIsNone(room.north)
        self.assertIsNone(room.south)

    def test_room_surrounded_wall(self):
        """壁に囲まれた部屋を作る
        """

        room = Room(room_number=1)
        room.west = Wall()
        room.east = Wall()
        room.north = Wall()
        room.south = Wall()

        self.assertIsInstance(room.west, Wall)

if __name__ == '__main__':
    unittest.main()