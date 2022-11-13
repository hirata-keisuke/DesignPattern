import unittest
from src.enchanted_maze_factory import EnchantedMazeFactory

class RoomTest(unittest.TestCase):

    def test_room_attributes(self):
        """部屋二つが東西をドアでつながる迷路を構成する
        """

        factory = EnchantedMazeFactory()
        maze = factory.make_maze()
        r1 = factory.make_room(1)
        r2 = factory.make_room(2)
        d = factory.make_door(r1, r2)
        
        maze.add_room(1, r1)
        maze.add_room(2, r2)

        r1.west = factory.make_wall()
        r1.east = d
        r1.south = factory.make_wall()
        r1.north = factory.make_wall()

        r2.west = d
        r2.east = factory.make_wall()
        r2.south = factory.make_wall()
        r2.north = factory.make_wall()

        self.assertEqual(r1, maze.rooms[1])
        self.assertEqual(r2, maze.rooms[2])

if __name__ == '__main__':
    unittest.main()