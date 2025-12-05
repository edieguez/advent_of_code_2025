#! /usr/bin/env python3

def parse_ranges_and_ids(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f if line.strip() or line == '\n']

	blank_index = lines.index('')
	range_lines = lines[:blank_index]
	id_lines = lines[blank_index+1:]
	ranges = []

	for line in range_lines:
		start, end = map(int, line.split('-'))
		ranges.append((start, end))

	ids = [int(line) for line in id_lines]

	return ranges, ids

def is_fresh(ingredient_id, ranges):
	return any(start <= ingredient_id <= end for start, end in ranges)

if __name__ == '__main__':
	ranges, ingredient_ids = parse_ranges_and_ids('input.txt')
	fresh_count = sum(1 for ingredient_id in ingredient_ids if is_fresh(ingredient_id, ranges))

	print(fresh_count)
