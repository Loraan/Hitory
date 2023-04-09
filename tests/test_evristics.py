import unittest
import os
import sys
import numpy as np


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


from moduls import evristics


class TestHitoriEvristics(unittest.TestCase):
    
    def setUp(self):
        self.hitory = evristics.check_all(field)

    def exception_field(self):
        field = [[1, 1, 1, 1], [1, 1, 1 ,1], [1, 1, 1, 1], [1, 1, 1]]
        self.assertRaises(IOError("Invalid input format"), self.hitory.solver(field))
        
    def test_no_solution_first(self):
        field_original = [[1, 1, 1, 1], [1, 1, 1 ,1], [1, 1, 1, 1], [1, 1, 1 ,1]]
        field_received = "no solution"
        self.assertEqual(self.solver(field_original), field_received)
        
    def test_no_solution_second(self):
        field_original = [[1, 1, 1, 3, 1], [1, 3, 4, 5, 6], [1, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        field_received = "no solution"
        self.assertEqual(self.solver(field_original), field_received)
        
    def test_no_solution_third(self):
        field_original = [[1, 1, 1, 3, 1, 1], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]]
        field_received = "no solution"
        self.assertEqual(self.solver(field_original), field_received)
        
    def test_no_solution_fourth(self):
        field_original = [[1, 1, 5, 1, 1], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        field_received = "no solution"
        self.assertEqual(self.solver(field_original), field_received)

    def test_nothing_to_change(self):
        field_original = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        field_received = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        self.assertEqual(self.solver(field_original), field_received)
        
    def test_triads_row(self):
        field_original = [[1, 1, 1, 2, 3], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        field_received = [[-1, 1, -1, 2, 3], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        self.assertEqual(self.solver(field_original), field_received)

    def test_duals_row(self):
        field_original = [[1, 1, 2, 3, 1], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        field_received = [[1, -1, 2, 3, -1], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        self.assertEqual(self.solver(field_original), field_received)

    def test_triads_column(self):
        field_original = [[1, 2, 3, 4, 5], [1, 3, 4, 5, 6], [1, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        field_received = [[-1, 2, 3, 4, 5], [1, 3, 4, 5, 6], [-1, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        self.assertEqual(self.solver(field_original), field_received)

    def test_duals_column(self):
        field_original = [[1, 2, 3, 4, 5], [1, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [1, 6, 7, 8, 9]]
        field_received = [[1, 2, 3, 4, 5], [-1, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [-1, 6, 7, 8, 9]]
        self.assertEqual(self.solver(field_original), field_received)
