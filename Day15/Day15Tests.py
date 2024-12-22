import unittest
from Part1 import moveLeft, moveRight, moveUp, moveDown, useInstructions, calcBoxes
from utils.utils import stringTo2DWithType, removeNewLines


class testMoves(unittest.TestCase):
    def testMoveLeftBlocked(self):
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

    def testMoveLeftClear(self):
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

    def testMoveLeftWithBox(self):
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

    def testMoveLeftBlockedWithBox(self):
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

    def testMoveRight(self):
        start = """########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""
        expected = """########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""

        self.assertEqual(stringTo2DWithType(expected, str), moveRight(stringTo2DWithType(start, str),3,1))

    def testMoveUp(self):
        start = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""
        expected = """########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""
        self.assertEqual(stringTo2DWithType(expected, str), moveUp(stringTo2DWithType(start, str),2,2))

    def testMoveDown(self):
        start = """########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""
        expected = """########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########"""
        self.assertEqual(stringTo2DWithType(expected, str), moveDown(stringTo2DWithType(start, str),4,1))

    def testUseInstructions(self):
        start = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""
        expected = """########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########"""

        instructions = list(removeNewLines(open("testInstructions.txt", "r").read()))
        self.assertEqual(stringTo2DWithType(expected, str), useInstructions(stringTo2DWithType(start, str), instructions))

class testBoxes(unittest.TestCase):
    def testCalcBoxes(self):
        larger = """##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########"""
        smaller = """########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########"""
        self.assertEqual(10092, calcBoxes(stringTo2DWithType(larger, str)))
        self.assertEqual(2028, calcBoxes(stringTo2DWithType(smaller, str)))






if __name__ == '__main__':
    unittest.main()
