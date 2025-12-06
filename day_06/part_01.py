#! /usr/bin/env python3

def parse_worksheet(filename):
	with open(filename) as f:
		lines = [line.rstrip('\n') for line in f]

	# Transpose the worksheet to columns
	max_len = max(len(line) for line in lines)
	padded_lines = [line.ljust(max_len) for line in lines]
	columns = [''.join(row[i] for row in padded_lines) for i in range(max_len)]

	# Find problem boundaries (columns of only spaces)
	boundaries = [i for i, col in enumerate(columns) if set(col) == {' '}]

	# Add start/end boundaries
	boundaries = [-1] + boundaries + [max_len]
	problems = []

	for b1, b2 in zip(boundaries, boundaries[1:]):
		if b2 - b1 <= 1:
			continue

		problem_cols = columns[b1+1:b2]

		# Each problem is a list of columns
		# Parse numbers (all but last row), operation (last row)
		numbers = []

		for row in range(len(lines)-1):
			num_str = ''.join(problem_cols).strip()
			num = ''.join(col[row] for col in problem_cols).strip()

			if num:
				numbers.append(int(num))

		op_row = len(lines)-1
		op = ''.join(col[op_row] for col in problem_cols).strip()

		if op == '+':
			result = sum(numbers)
		elif op == '*':
			result = 1

			for n in numbers:
				result *= n
		else:
			continue

		problems.append(result)

	return problems

if __name__ == '__main__':
	results = parse_worksheet('input.txt')

	print(sum(results))
