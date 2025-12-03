#! /usr/bin/env python3

def is_repeated_twice(n: int) -> bool:
	s = str(n)
	l = len(s)

	if l % 2 != 0:
		return False

	half = l // 2

	return s[:half] == s[half:]

if __name__ == '__main__':
	with open('input.txt') as f:
		line = f.read().strip()

	total = 0

	for part in line.split(','):
		if not part:
			continue

		start, end = map(int, part.split('-'))

		for n in range(start, end + 1):
			if is_repeated_twice(n):
				total += n

	print(total)
