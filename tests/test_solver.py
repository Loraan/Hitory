import unittest
import os
import sys
import numpy as np


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


from moduls import solver 


class TestHitoriSolver(unittest.TestCase):
    
    def setUp(self):
        dual_field = np.array([[0]*5]*5) 
        self.solver= solver.solution(dual_field)

##    def test_squares_in_angle(self):
##        field_original = [[1, 1, 3, 4, 5], [1, 1, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
##        field_received = [[-1, 1, 3, 4, 5], [1, -1, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
##        self.assertEqual(self.solver(field_original), field_received)
##
##    def test_squares_not_in_angle(self):
##        field_original = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 10, 10, 6, 7], [4, 10, 10, 7, 8], [5, 6, 7, 8, 9]]
##        field_received = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, -1, 10, 6, 7], [4, 10, -1, 7, 8], [5, 6, 7, 8, 9]]
##        self.assertEqual(self.solver(field_original), field_received)
##        
##    def test_solution_first(self):
##        field_original = [[3, 3, 4, 4, 5], [1, 5, 2, 3, 4], [2, 5, 5, 1, 1], [5, 2, 3, 5, 1], [5, 3, 3, 4, 4]]
##        field_received = [[3, -1, 4, -1, 5], [1, 5, 2, 3, 4], [2, -1, 5, 1, -1], [-1, 2 , 3, 5, 1], [5, 3, -1, 4, -1]]
##        self.assertEqual(self.solver(field_original), field_received)

    def test_solution_second(self):
        field_original = np.array([[2, 1, 4, 1, 2], [3, 4, 1, 1, 5], [1, 1, 5, 2, 4], [4, 2, 1, 2, 3], [2, 2, 3, 4, 3]])
        field_received = [[-1, 1, 4, -1, 2], [3, 4, -1, 1, 5], [1, -1, 5, 2, 4], [4, 2 , 1, -1, 3], [2, -1, 3, 4, -1]]
        self.assertEqual(self.solver(field_original), field_received)

    def test_solution_third(self):
        field_original = [[1, 5, 1, 2, 3], [1, 4, 5, 5, 1], [3, 3, 5, 4, 1], [3, 2, 1, 1, 3], [5, 5, 2, 3, 4]]
        field_received = [[-1, 5, 1, 2, 3], [1, 4, -1, 5, -1], [-1, 3, 5, 4, 1], [3, 2, -1, 1, -1], [5, -1, 2, 3, 4]]
        self.assertEqual(self.solver(field_original), field_received)

    def test_solution_fourth(self):
        field_original = [[4, 3, 1, 4, 5], [5, 4, 5, 1, 4], [1, 2, 4, 4, 1], [1, 4, 2, 3, 4], [4, 1, 5, 1, 3]]
        field_received = [[-1, 3, 1, 4, 5], [5, 4, -1, 1, -1], [-1, 2, 4, -1, 1], [1, -1, 2, 3, 4], [4, 1, 5, -1, 3]]
        self.assertEqual(self.solver(field_original), field_received)

    def test_solution_fifth(self):
        field_original = [[8, 4, 1, 3, 5, 2, 3, 4], [5, 5, 8, 7, 6, 4, 5, 1], [1, 3, 5, 3, 3, 3, 8, 2], [2, 7, 3, 8, 7, 5, 1, 2], [7, 4, 6, 1, 4, 8, 7, 3], [5, 3, 6, 6, 6, 1, 2, 4], [6, 3, 2, 3, 1, 2, 4, 8], [4, 1, 8, 2, 4, 3, 5, 5]]
        field_received = [[8, 4, 1, -1, 5, 2, 3, -1], [-1, 5, 8, 7, 6, 4, -1, 1], [1, -1, 5, -1, 3, -1, 8, 2], [2, 7, 3, 8, -1, 5, 1, -1], [7, -1, 6, 1, 4, 8, -1, 3], [5, 3, -1, 6, -1, 1, 2, 4], [6, -1, 2, 3, 1, -1, 4, 8], [4, 1, -1, 2, -1, 3, 5, -1]]
        self.assertEqual(self.solver(field_original), field_received)

    def test_solution_sixth(self):
        field_original = [[3, 1, 5, 2, 2], [2, 3, 1, 1, 2], [2, 5, 1, 4, 1], [5, 4, 2, 1, 3], [3, 2, 2, 3, 2]]
        field_received = [[3, 1, 5, 2, -1], [-1, 3, 1, -1, 2], [2, 5, -1, 4, 1], [5, 4, 2, 1, 3], [-1, 2, -1, 3, -1]]
        self.assertEqual(self.solver(field_original), field_received)

    def test_solution_seventh(self):
        field_original = [[3, 2, 4, 1, 2], [2, 4, 3, 3, 3], [1, 2, 3, 5, 1], [5, 1, 5, 4, 1], [1, 4, 5, 2, 4]]
        field_received = [[3, -1, 4, 1, 2], [2, 4, -1, 3, -1], [-1, 2, 3, 5, 1], [5, 1, -1, 4, -1], [1, -1, 5, 2, 4]]
        self.assertEqual(self.solver(field_original), field_received)

    def test_solution_eightht(self):
        field_original = [[2, 2, 5, 1, 5], [1, 4, 3, 1, 5], [3, 1, 1, 4, 2], [2, 1, 2, 3, 3], [5, 2, 4, 3, 3]]
        field_received = [[2, -1, 5, 1, -1], [1, 4, 3, -1, 5], [3, -1, 1, 4, 2], [-1, 1, 2, -1, 3], [5, 2, 4, 3, -1]]
        self.assertEqual(self.solver(field_original), field_received)

if __name__ == "__main__":
 unittest.main()
