import unittest
from utils.utils import txtTo2DWithType, reverse2DHorizontal, removeNewLines, changeLType, findCharIn2DArray, stringTo2DWithType


class TestUtils(unittest.TestCase):

    def testChangeLTypesInt(self):
        result = changeLType(["123", "321"], int)
        self.assertEqual([123, 321],  result)  # add assertion here

    def testTxtTo2DWithType(self):
        self.assertEqual([[1,2,3],[2,3,4],[3,4,5],[4,5,6]], txtTo2DWithType(
            "utils/testDigitsTxtTo2DWithType.txt", int))
        self.assertEqual([["1","2","3"],["2","3","4"],["3","4","5"],["4","5","6"]], txtTo2DWithType(
            "utils/testDigitsTxtTo2DWithType.txt", str))

    def testRemoveNewLines(self):
        testInput = """<><><>()()(
{}{}{}[][][]
qeqeqeq
12q4"""
        self.assertEqual("<><><>()()({}{}{}[][][]qeqeqeq12q4", removeNewLines(testInput))

    def testFindCharIn2DArray(self):
        self.assertEqual([2,2], findCharIn2DArray(txtTo2DWithType("Day15/testWarehouse.txt", str), "@"))

    def testReverse2DHorizontal(self):
        self.assertEqual([["1","2","3"],["2","3","4"],["3","4","5"],["4","5","6"]], reverse2DHorizontal([["3","2","1"],["4","3","2"],["5","4","3"],["6","5","4"]]))

    def testStringTo2DWithType(self):
        testData = """#######
#...O..
#......"""
        self.assertEqual([["#", "#", "#", "#", "#", "#", "#"], ["#", ".", ".", ".", "O", ".", "."], ["#", ".", ".", ".", ".", ".", "."]], stringTo2DWithType(testData, str))

if __name__ == '__main__':
    unittest.main()
