

def valid_coloring(
    neighbours: list[int], colored_vertices: list[int], color: int
) -> bool:

    # Does any neighbour not satisfy the constraints
    return not any(
        neighbour == 1 and colored_vertices[i] == color
        for i, neighbour in enumerate(neighbours)
    )


def util_color(
    graph: list[list[int]], max_colors: int, colored_vertices: list[int], index: int
) -> bool:

    # Base Case
    if index == len(graph):
        return True

    # Recursive Step
    for i in range(max_colors):
        if valid_coloring(graph[index], colored_vertices, i):
            # Color current vertex
            colored_vertices[index] = i
            # Validate coloring
            if util_color(graph, max_colors, colored_vertices, index + 1):
                return True
            # Backtrack
            colored_vertices[index] = -1
    return False


def color(graph: list[list[int]], max_colors: int) -> list[int]:
    
    colored_vertices = [-1] * len(graph)

    if util_color(graph, max_colors, colored_vertices, 0):
        return colored_vertices

    return []
