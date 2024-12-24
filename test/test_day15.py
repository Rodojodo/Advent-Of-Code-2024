import unittest

from Day15.Part1 import moveLeft, moveRight, moveUp, moveDown, useInstructions, calcBoxes
from Day15.Part2 import scaleWarehouse, bigMoveLeft, bigMoveRight, bigMoveUp, bigMoveDown, moveBigBoxUp, checkMoveUpSafe, useBigInstructions
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

        f = open("Day15/testInstructions.txt", "r")
        instructions = list(removeNewLines(f.read()))
        f.close()
        self.assertEqual(stringTo2DWithType(expected, str), useInstructions(stringTo2DWithType(start, str), instructions))

    def testBigMoveLeftWithBox(self):
        start = """##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############"""
        expected = """##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############"""
        self.assertEqual(stringTo2DWithType(expected, str), bigMoveLeft(stringTo2DWithType(start, str), 10, 3))

    def testBigMoveLeftClear(self):
        start = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############"""
        expected = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############"""
        self.assertEqual(stringTo2DWithType(expected, str), bigMoveLeft(stringTo2DWithType(start, str), 9, 5))

    def testBigMoveUpWithBox(self):
        start = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############"""
        expected = """##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############"""

        self.assertEqual(stringTo2DWithType(expected, str), bigMoveUp(stringTo2DWithType(start, str), 7, 5))

    def testBigMoveUpWithBoxBlocked(self):
        expected = """##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############"""
        self.assertEqual(stringTo2DWithType(expected, str), bigMoveUp(stringTo2DWithType(expected, str), 7, 4))

    def testBigMoveDown(self):
        start = """##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############"""
        expected = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############"""

        self.assertEqual(stringTo2DWithType(expected, str), bigMoveDown(stringTo2DWithType(start, str), 9, 4))

    def testBigMoveRight(self):
        start = """##############
##......##..##
##..........##
##...[][]...##
##....[]@...##
##..........##
##############"""
        expected = """##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############"""
        self.assertEqual(stringTo2DWithType(expected, str), bigMoveRight(stringTo2DWithType(start, str), 8, 4))

    def testMoveBigBoxUp(self):
        start = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##..........##
##############"""
        expected = """##############
##......##..##
##...[][]...##
##....[]....##
##..........##
##..........##
##############"""
        self.assertEqual(stringTo2DWithType(expected, str), moveBigBoxUp(stringTo2DWithType(start, str), 6, 4))
        self.assertEqual(stringTo2DWithType(expected, str), moveBigBoxUp(stringTo2DWithType(start, str), 7, 4))

    def testCheckMoveUpSafe(self):
        clear = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##..........##
##############"""
        notClear = """##############
##......##..##
##...[][]...##
##....[]....##
##..........##
##..........##
##############"""
        self.assertTrue(True, checkMoveUpSafe(stringTo2DWithType(clear, str), 6, 4))
        self.assertTrue(True, checkMoveUpSafe(stringTo2DWithType(clear, str), 7, 4))
        self.assertEqual(False, checkMoveUpSafe(stringTo2DWithType(notClear, str), 6, 3))
        self.assertEqual(False, checkMoveUpSafe(stringTo2DWithType(notClear, str), 7, 3))

    def testUseBigInstructions(self):
        start = """##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############"""
        expected = """##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############"""

        f = open("Day15/testPart2Instructions.txt", "r")
        instructions = list(removeNewLines(f.read()))
        f.close()
        self.assertEqual(stringTo2DWithType(expected, str), useBigInstructions(stringTo2DWithType(start, str), instructions))

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
        self.assertEqual(10092, calcBoxes(stringTo2DWithType(larger, str), "O"))
        self.assertEqual(2028, calcBoxes(stringTo2DWithType(smaller, str), "O"))

class testPart2(unittest.TestCase):
    def testScaleWarehouse(self):
        f = open("Day15/testPart2Warehouse.txt", "r")
        warehouse = f.read()
        f.close()
        stretchedWarehouse = stringTo2DWithType("""##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############""", str)

        self.assertEqual(stretchedWarehouse, scaleWarehouse(stringTo2DWithType(warehouse, str)))


if __name__ == '__main__':
    unittest.main()
