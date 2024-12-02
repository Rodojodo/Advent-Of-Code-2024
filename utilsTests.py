import unittest
import utils


class TestUtils(unittest.TestCase):

    def testChangeLTypesInt(self):
        result = utils.changeLType(["123", "321"], int)
        self.assertEqual([123, 321],  result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
