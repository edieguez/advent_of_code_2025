#! /usr/bin/env python3

def decode(filename: str) -> int:
    index = 50
    operations: list[int] = []
    password = 0

    with open(filename, "r") as file:
        for line in file.readlines():
            operation = line[0].upper()
            value = int(line[1:])

            if operation == "R":
                operations.append(value)
            elif operation == "L":
                operations.append(-value)

    for operation in operations:
        index = ((index + operation) % 100 + 100) % 100
        print(f"Operation: {operation}, New index: {index}")
        password += 1 if index == 0 else 0

    return password

if __name__ == "__main__":
    result = decode("input.txt")
    print(f"Decoded value: {result}")
