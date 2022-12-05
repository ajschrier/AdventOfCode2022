def fully_overlaps(input_line):
	# keys = [i for i in input_line if i.isalnum()]
	keys = [pair.split('-') for pair in input_line.split(',')]


	if keys[0][0] <= keys[1][0]:
		lower_idx_range = (int(keys[0][0]), int(keys[0][1]))
		higher_idx_range = (int(keys[1][0]), int(keys[1][1].strip()))
	else:
		higher_idx_range = (int(keys[0][0]), int(keys[0][1]))
		lower_idx_range = (int(keys[1][0]), int(keys[1][1].strip()))

	top_overlaps = (lower_idx_range[0] <= higher_idx_range[0]) and (higher_idx_range[1] <= lower_idx_range[1])
	bottom_overlaps = (lower_idx_range[0] >= higher_idx_range[0]) and (higher_idx_range[1] >= lower_idx_range[1])
	
	overlaps = top_overlaps or bottom_overlaps

	# print(lower_idx_range, higher_idx_range, overlaps)
	
	return overlaps

def partial_overlaps(input_line):
	keys = [pair.split('-') for pair in input_line.split(',')]


	if int(keys[0][0]) <= int(keys[1][0]):
		lower_idx_range = (int(keys[0][0]), int(keys[0][1]))
		higher_idx_range = (int(keys[1][0]), int(keys[1][1].strip()))
	else:
		higher_idx_range = (int(keys[0][0]), int(keys[0][1]))
		lower_idx_range = (int(keys[1][0]), int(keys[1][1].strip()))

	top_overlaps = (lower_idx_range[0] <= higher_idx_range[0]) or (higher_idx_range[1] >= lower_idx_range[1])
	bottom_overlaps = (lower_idx_range[1] >= higher_idx_range[0]) or (higher_idx_range[1] <= lower_idx_range[0])
	
	overlaps = top_overlaps and bottom_overlaps
	if not overlaps:
		print(lower_idx_range, higher_idx_range, overlaps)
	return overlaps

def overlap_count(input_list):
	count = 0
	for line in input_list:
		if fully_overlaps(line):
			count += 1
	return count

def partial_overlap_count(input_list):
	count = 0
	for line in input_list:
		if partial_overlaps(line):
			count += 1
	return count

if __name__ == '__main__':
	with open("input.txt", "r") as f:
		input_list = f.readlines()

	print(overlap_count(input_list))
	# 566: too high
	# 328: too low
	# 462: incorrect
	# 521: incorrect

	print(partial_overlap_count(input_list))
	# 809: too low

