import unittest
from src.room import Room

class RoomTest(unittest.TestCase):

    def test_room_attributes(self):
        """迷路を構成する部屋が想定している属性を持つことを確認する
        """

        room = Room(room_number=1)

        self.assertEqual(1, room.number)


if __name__ == '__main__':
    unittest.main()