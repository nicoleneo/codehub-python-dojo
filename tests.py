import unittest
from dojo import Board
import numpy as np

class Test_Place_Ship(unittest.TestCase):
    def test_place_horizontal(self):
        correct = np.zeros(shape=(10,10))
        correct[1,:] =  np.array([0,3,3,3,0,0,0,0,0,0])
        b = Board()
        b.place_ship('cruser', 'hor', 2, 'b')
        np.testing.assert_almost_equal(correct, b.board)

    def test_place_vertical(self):
        correct = np.zeros(shape=(10,10))
        correct[:,3] =  np.array([0,4,4,4,0,0,0,0,0,0])
        b = Board()
        b.place_ship('submarine', 'ver', 2, 'd')
        np.testing.assert_almost_equal(correct, b.board)

    def test_hit(self):
        b = Board()
        b.place_ship('cruser', 'hor', 1, 'a')
        self.assertTrue(b.hit(1,'a'))

    def test_ship_on_ship(self):
        with self.assertRaises(ValueError):
            b = Board()
            b.place_ship('cruser', 'hor', 1, 'a')
            b.place_ship('cruser', 'hor', 1, 'a')

if __name__=='__main__':
    unittest.main()


