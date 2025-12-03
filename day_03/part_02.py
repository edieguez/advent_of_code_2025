#! /usr/bin/env python3

def max_joltage_from_bank_12(battery_bank: str) -> int:
	digits = [int(d) for d in battery_bank.strip()]

	if len(digits) < 12:
		return 0

	selected = []
	start = 0
	remaining = 12

	while remaining > 0:
		end = len(digits) - remaining + 1
		max_digit = max(digits[start:end])
		idx = digits.index(max_digit, start, end)
		selected.append(str(digits[idx]))
		start = idx + 1
		remaining -= 1

	return int(''.join(selected))

if __name__ == '__main__':
	with open('input.txt') as input_file:
		battery_banks = input_file.readlines()

	total_output_joltage = sum(max_joltage_from_bank_12(bank) for bank in battery_banks)

	print(total_output_joltage)