
from __future__ import annotations


def depth_first_search(
    possible_board: list[int],
    diagonal_right_collisions: list[int],
    diagonal_left_collisions: list[int],
    boards: list[list[str]],
    n: int,
) -> None:


    # Get next row in the current board (possible_board) to fill it with a queen
    row = len(possible_board)

    if row == n:
        boards.append([". " * i + "Q " + ". " * (n - 1 - i) for i in possible_board])
        return

    for col in range(n):

        if (
            col in possible_board
            or row - col in diagonal_right_collisions
            or row + col in diagonal_left_collisions
        ):
            continue

        # If it is False we call dfs function again and we update the inputs
        depth_first_search(
            possible_board + [col],
            diagonal_right_collisions + [row - col],
            diagonal_left_collisions + [row + col],
            boards,
            n,
        )


def n_queens_solution(n: int) -> None:
    boards: list[list[str]] = []
    depth_first_search([], [], [], boards, n)

    # Print all the boards
    for board in boards:
        for column in board:
            print(column)
        print("")

    print(len(boards), "solutions were found.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n_queens_solution(4)
