from __future__ import annotations


def solve_maze(maze: list[list[int]]) -> bool:

    size = len(maze)
    # We need to create solution object to save path.
    solutions = [[0 for _ in range(size)] for _ in range(size)]
    solved = run_maze(maze, 0, 0, solutions)
    if solved:
        print("\n".join(str(row) for row in solutions))
    else:
        print("No solution exists!")
    return solved


def run_maze(maze: list[list[int]], i: int, j: int, solutions: list[list[int]]) -> bool:
    size = len(maze)
    # Final check point.
    if i == j == (size - 1):
        solutions[i][j] = 1
        return True

    lower_flag = (not (i < 0)) and (not (j < 0))  # Check lower bounds
    upper_flag = (i < size) and (j < size)  # Check upper bounds

    if lower_flag and upper_flag:
        # check for already visited and block points.
        block_flag = (not (solutions[i][j])) and (not (maze[i][j]))
        if block_flag:
            # check visited
            solutions[i][j] = 1

            # check for directions
            if (
                run_maze(maze, i + 1, j, solutions)
                or run_maze(maze, i, j + 1, solutions)
                or run_maze(maze, i - 1, j, solutions)
                or run_maze(maze, i, j - 1, solutions)
            ):
                return True

            solutions[i][j] = 0
            return False
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
