def rucksack_priority(test_input):
	total_value = 0
	for line in test_input:
		midpoint = len(line) // 2
		compartments = (line[:midpoint], line[midpoint:])
		matches = set([i for i in compartments[0] if i in compartments[1]])
		for match in matches:
			total_value += priority_value(match)
	return total_value

def priority_value(char):
	if char.islower():
		return ord(char) - 96
	elif char.isupper():
		return ord(char) - 38
	return 0

def rucksack_group_priority(test_input):
	total_value = 0
	groups = len(test_input) // 3
	for group in range(groups):
		idx = 3 * group
		packs = [test_input[idx],
				test_input[idx+1],
				test_input[idx+2]]
		first_matches = set([i for i in packs[0] if i in packs[1]])
		full_matches = set([i for i in packs[2] if i in first_matches])
		for match in full_matches:
				total_value += priority_value(match)
	return total_value

if __name__ == '__main__':
	with open("input.txt", "r") as f:
		puzzle_input = f.readlines()

	print(rucksack_priority(puzzle_input))
	print(rucksack_group_priority(puzzle_input))