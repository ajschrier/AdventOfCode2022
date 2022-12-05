import unittest
import Day3

class Day3Tests(unittest.TestCase):
	demo_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

	def test_rucksack_priority(self):
		test_input = self.demo_input.split('\n')
		self.assertEqual(Day3.rucksack_priority(test_input), 157)

	def test_priority_value(self):
		self.assertEqual(Day3.priority_value('a'), 1)
		self.assertEqual(Day3.priority_value('p'), 16)
		self.assertEqual(Day3.priority_value('A'), 27)
		self.assertEqual(Day3.priority_value('r'), 18)
		self.assertEqual(Day3.priority_value('Z'), 52)

	def test_rucksack_group_priority(self):
		test_input = self.demo_input.split('\n')
		self.assertEqual(Day3.rucksack_group_priority(test_input), 70)



if __name__ == '__main__':
	unittest.main()