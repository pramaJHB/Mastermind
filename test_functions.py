import unittest
from unittest.mock import patch
from io import StringIO
from test_base import captured_io
import mastermind

class TestFunctions(unittest.TestCase):

    def test_create_code(self):
        for x in range(100):
            result = mastermind.create_code()
            self.assertEqual(len(result), 4)
            for i in range(0, 4):
                self.assertTrue(1 <= result[i] <= 8)


    def test_check_correctness(self):
        self.assertEqual(mastermind.check_correctness(5, 4), True)
        self.assertEqual(mastermind.check_correctness(6, 1), False)
        self.assertEqual(mastermind.check_correctness(9, 0), False)
        self.assertEqual(mastermind.check_correctness(2, 4), True)
        self.assertEqual(mastermind.check_correctness(12, 2), False)
        self.assertEqual(mastermind.check_correctness(12, 4), True)
        self.assertEqual(mastermind.check_correctness(1, 3), False)
        self.assertEqual(mastermind.check_correctness(10, 4), True)
        self.assertEqual(mastermind.check_correctness(11, 4), True)
        self.assertEqual(mastermind.check_correctness(7, 5), False)


    @patch("sys.stdin", StringIO("54\njh45\n874316\n0854\n1234\n3896\niyte\n3251\n"))
    def test_get_answer_input(self):
        self.assertEqual(mastermind.get_answer_input(), "1234")
        self.assertEqual(mastermind.get_answer_input(), "3251")
        
        with captured_io(StringIO("54\n874316\n258\n1234\n386\n3251\n")) as (out, err):
            mastermind.get_answer_input()
        output = out.getvalue().strip()
        self.assertEqual("""Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code:""", output)
        

    @patch("sys.stdin", StringIO("1234\n4251\n8753\n4185\n2413\n4231"))
    def test_take_turn(self):
        self.assertEqual(mastermind.take_turn([4, 2, 3, 1]), (2, 2))
        self.assertEqual(mastermind.take_turn([4, 2, 3, 1]), (3, 0))
        self.assertEqual(mastermind.take_turn([4, 2, 3, 1]), (0, 1))
        self.assertEqual(mastermind.take_turn([4, 2, 3, 1]), (1, 1))
        self.assertEqual(mastermind.take_turn([4, 2, 3, 1]), (0, 4))
        self.assertEqual(mastermind.take_turn([4, 2, 3, 1]), (4, 0))


if __name__ == '__main__':
    unittest.main()