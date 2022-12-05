def rps_score(test_input):
	total_score = 0
	for item in test_input:
		# A for Rock, B for Paper, and C for Scissors.
		their_move = item[0]

		# X for Rock, Y for Paper, and Z for Scissors
		my_move = item[2]

		our_selection_score = {'X': 1, 'Y': 2, 'Z': 3}

		outcome_score = {
		'X' : { # Rock
			'A': 3,
			'B': 0,
			'C': 6
			},
		'Y' : { # Paper
			'A': 6,
			'B': 3,
			'C': 0
			},
		'Z' : { # Scissors
			'A': 0,
			'B': 6,
			'C': 3
			},
		}

		move_score = our_selection_score[my_move] + outcome_score[my_move][their_move]

		total_score += move_score

	return total_score

def rps_score_part2(test_input):
	total_score = 0
	for item in test_input:
		# A for Rock, B for Paper, and C for Scissors.
		their_move = item[0]

		# X for Rock, Y for Paper, and Z for Scissors
		my_result = item[2]

		our_selection_score = {'X': 1, 'Y': 2, 'Z': 3}

		my_move_dict = {
		'X' : { # Loss
			'A': 'Z',
			'B': 'X',
			'C': 'Y'
			},
		'Y' : { # Draw
			'A': 'X',
			'B': 'Y',
			'C': 'Z'
			},
		'Z' : { # Win
			'A': 'Y',
			'B': 'Z',
			'C': 'X'
			},
		}

		outcome_score = {
		'X' : { # Rock
			'A': 3,
			'B': 0,
			'C': 6
			},
		'Y' : { # Paper
			'A': 6,
			'B': 3,
			'C': 0
			},
		'Z' : { # Scissors
			'A': 0,
			'B': 6,
			'C': 3
			},
		}

		my_move = my_move_dict[my_result][their_move]
		move_score = our_selection_score[my_move] + outcome_score[my_move][their_move]

		total_score += move_score

	return total_score

if __name__ == '__main__':
	with open("input.txt", "r") as f:
		puzzle_input = f.readlines()

	print(rps_score(puzzle_input))
	print(rps_score_part2(puzzle_input))