import unittest
from Part1 import moveLeft
from utils.utils import stringTo2DWithType


class Part1Tests(unittest.TestCase):
    def testMoveLeft(self):
        # Get blocked by wall
        self.assertEqual(stringTo2DWithType("""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""", str), moveLeft(stringTo2DWithType("""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""", str), 2,2))

        # Move into clear space
        self.assertEqual(stringTo2DWithType("""########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########""", str), moveLeft(stringTo2DWithType("""########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########""", str), 4,2))

        # Move Box into clear space
        self.assertEqual(stringTo2DWithType("""########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########""", str), moveLeft(stringTo2DWithType("""########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########""", str), 5,4))

        # Move box blocked by wall
        self.assertEqual(stringTo2DWithType("""########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########""", str), moveLeft(stringTo2DWithType("""########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########""", str),4,4))



if __name__ == '__main__':
    unittest.main()
