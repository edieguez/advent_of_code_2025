#! /usr/bin/env python3

def is_repeated_pattern(n: int) -> bool:
	s = str(n)
	l = len(s)

	# Try all possible substring lengths from 1 up to half the length
	for size in range(1, l // 2 + 1):
		if l % size != 0:
			continue

		pattern = s[:size]

		if pattern * (l // size) == s:
			return True

	return False

if __name__ == '__main__':
	with open('input.txt') as f:
		line = f.read().strip()

	total = 0

	for part in line.split(','):
		if not part:
			continue

		start, end = map(int, part.split('-'))

		for n in range(start, end + 1):
			if is_repeated_pattern(n):
				total += n

	print(total)
