

def check_cycle(graph: dict) -> bool:

    # Keep track of visited nodes
    visited: set[int] = set()
    # To detect a back edge, keep track of vertices currently in the recursion stack
    rec_stk: set[int] = set()
    for node in graph:
        if node not in visited:
            if depth_first_search(graph, node, visited, rec_stk):
                return True
    return False


def depth_first_search(graph: dict, vertex: int, visited: set, rec_stk: set) -> bool:

    # Mark current node as visited and add to recursion stack
    visited.add(vertex)
    rec_stk.add(vertex)

    for node in graph[vertex]:
        if node not in visited:
            if depth_first_search(graph, node, visited, rec_stk):
                return True
        elif node in rec_stk:
            return True

    # The node needs to be removed from recursion stack before function ends
    rec_stk.remove(vertex)
    return False


if __name__ == "__main__":
    from doctest import testmod

    testmod()
