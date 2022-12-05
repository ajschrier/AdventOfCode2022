import unittest
import Day2

class Day2Tests(unittest.TestCase):

	demo_input = '''A Y
B X
C Z'''
	def test_rps_score_first_line(self):
		test_input = ['A Y']
		self.assertEqual(Day2.rps_score(test_input), 8)

	def test_rps_score(self):
		test_input = self.demo_input.split('\n')
		# print(test_input)
		self.assertEqual(Day2.rps_score(test_input), 15)

	def test_rps_score_part2(self):
		test_input = self.demo_input.split('\n')
		# print(test_input)
		self.assertEqual(Day2.rps_score_part2(test_input), 12)

	def test_rps_score__part2_first_line(self):
		test_input = ['A Y']
		self.assertEqual(Day2.rps_score_part2(test_input), 4)

if __name__ == '__main__':
	unittest.main()