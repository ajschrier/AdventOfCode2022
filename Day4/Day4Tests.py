import unittest
import Day4

class Day4Tests(unittest.TestCase):
	demo_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

	def test_fully_overlaps(self):
		self.assertTrue(Day4.fully_overlaps("2-8,3-7"))
		self.assertTrue(Day4.fully_overlaps("6-6,4-6"))
		self.assertTrue(Day4.fully_overlaps("1-93,2-11"))
		self.assertTrue(Day4.fully_overlaps("26-94,26-94"))
		self.assertTrue(Day4.fully_overlaps("66-85,66-86"))

	def test_does_not_fully_overlap(self):
		self.assertFalse(Day4.fully_overlaps("2-3,4-5"))
		self.assertFalse(Day4.fully_overlaps("5-7,7-9"))
		self.assertFalse(Day4.fully_overlaps("2-6,4-8"))
		self.assertFalse(Day4.fully_overlaps("92-92,7-91"))
		self.assertFalse(Day4.fully_overlaps("5-75,3-3"))
		self.assertFalse(Day4.fully_overlaps("36-37,37-52"))
		self.assertFalse(Day4.fully_overlaps("94-96,81-95"))
		self.assertFalse(Day4.fully_overlaps("1-1,2-98"))

	def test_partial_overlaps(self):
		self.assertTrue(Day4.partial_overlaps("5-7,7-9"))
		self.assertTrue(Day4.partial_overlaps("2-8,3-7"))
		self.assertTrue(Day4.partial_overlaps("6-6,4-6"))
		self.assertTrue(Day4.partial_overlaps("2-6,4-8"))
		self.assertTrue(Day4.partial_overlaps("1-83,1-84"))
		self.assertTrue(Day4.partial_overlaps("1-98,1-98"))

	def test_does_not_partially_overlap(self):
		self.assertFalse(Day4.partial_overlaps("2-4,6-8"))
		self.assertFalse(Day4.partial_overlaps("2-3,4-5"))
		self.assertFalse(Day4.partial_overlaps("1-1,2-98"))
		self.assertFalse(Day4.partial_overlaps("9-9,10-98"))
		self.assertFalse(Day4.partial_overlaps("22-70,78-90"))


	def test_overlap_count(self):
		test_input = self.demo_input.split('\n')
		self.assertEqual(Day4.overlap_count(test_input), 2)

	def test_partial_overlap_count(self):
		test_input = self.demo_input.split('\n')
		self.assertEqual(Day4.partial_overlap_count(test_input), 4)


if __name__ == '__main__':
	unittest.main()