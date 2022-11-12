import unittest
from src.wall import Wall

class WallTest(unittest.TestCase):

    def test_wall_enter(self):
        """壁のenterメソッドを呼び出すと引き返させられる
        """

        wall = Wall()

        self.assertEqual("引き返す", wall.enter())

if __name__ == "__main__":
    unittest.main()