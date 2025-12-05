#! /usr/bin/env python3

# Function to parse only the fresh ingredient ID ranges from the input file
def parse_ranges(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f if line.strip() or line == '\n']

	blank_index = lines.index('')
	range_lines = lines[:blank_index]
	ranges = []

	for line in range_lines:
		start, end = map(int, line.split('-'))
		ranges.append((start, end))

	return ranges

# Function to merge overlapping and adjacent ranges
def merge_ranges(ranges):
	if not ranges:
		return []

	sorted_ranges = sorted(ranges)
	merged = [sorted_ranges[0]]

	for current in sorted_ranges[1:]:
		last_start, last_end = merged[-1]
		current_start, current_end = current

		if current_start <= last_end + 1:
			merged[-1] = (last_start, max(last_end, current_end))
		else:
			merged.append(current)

	return merged

if __name__ == '__main__':
	ranges = parse_ranges('input.txt')
	merged = merge_ranges(ranges)
	total_fresh_ids = sum(end - start + 1 for start, end in merged)

	print(total_fresh_ids)
