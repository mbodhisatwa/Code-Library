
from __future__ import annotations

__author__ = "Alexander Joslin"


def min_steps_to_one(number: int) -> int:

    if number <= 0:
        raise ValueError(f"n must be greater than 0. Got n = {number}")

    table = [number + 1] * (number + 1)

    # starting position
    table[1] = 0
    for i in range(1, number):
        table[i + 1] = min(table[i + 1], table[i] + 1)
        # check if out of bounds
        if i * 2 <= number:
            table[i * 2] = min(table[i * 2], table[i] + 1)
        # check if out of bounds
        if i * 3 <= number:
            table[i * 3] = min(table[i * 3], table[i] + 1)
    return table[number]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
