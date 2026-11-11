#!/usr/bin/env python3
"""Print the Collatz sequence starting at 27 and the number of steps to reach 1."""


def collatz_sequence(start):
    """Return the Collatz sequence from start down to 1, inclusive."""
    if start < 1:
        raise ValueError("start must be a positive integer")
    sequence = [start]
    n = start
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz_sequence(27)
    for n in sequence:
        print(n)
    # Steps are transitions between values, so the initial value is not counted.
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
