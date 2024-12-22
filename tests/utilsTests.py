import unittest
from utils import utils
from utils.utils import txtTo2DWithType


class TestUtils(unittest.TestCase):

    def testChangeLTypesInt(self):
        result = utils.changeLType(["123", "321"], int)
        self.assertEqual([123, 321],  result)  # add assertion here

    def testTxtTo2DWithType(self):
        self.assertEqual([[1,2,3],[2,3,4],[3,4,5],[4,5,6]], utils.txtTo2DWithType("testDigitsTxtTo2DWithType.txt", int))
        self.assertEqual([["1","2","3"],["2","3","4"],["3","4","5"],["4","5","6"]], utils.txtTo2DWithType("testDigitsTxtTo2DWithType.txt", str))

    def testRemoveNewLines(self):
        testInput = """<><><>()()(
{}{}{}[][][]
qeqeqeq
12q4"""
        self.assertEqual("<><><>()()({}{}{}[][][]qeqeqeq12q4", utils.removeNewLines(testInput))

    def testFindCharIn2DArray(self):
        self.assertEqual([2,2], utils.findCharIn2DArray(txtTo2DWithType("../Day15/testWarehouse.txt", str), "@"))





if __name__ == '__main__':
    unittest.main()
