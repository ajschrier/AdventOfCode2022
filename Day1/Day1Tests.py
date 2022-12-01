import unittest
import Day1

class Day1Tests(unittest.TestCase):
    demo_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


    def test_max_calorie_count(self):
        test_input = self.demo_input.split('\n')

        self.assertEqual(Day1.max_calorie_count(test_input), 24000)

    def test_top_three_calorie_counts(self):
        test_input = self.demo_input.split('\n')
        
        self.assertEqual(Day1.top_three_calorie_count(test_input), 45000)


if __name__ == '__main__':
    unittest.main()