import heapq

def a_star(graph, start, goal, h):
    open_set = []
    heapq.heappush(open_set, (0 + h[start], 0, start, [start]))
    visited = set()

    while open_set:
        f, g, node, path = heapq.heappop(open_set)

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbour, cost in graph[node]:  # Corrected loop
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbour]
                heapq.heappush(open_set, (new_f, new_g, neighbour, path + [neighbour]))  # Correct indentation

    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

h = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 2,
    'F': 4,
    'G': 0
}

start = 'A'
goal = 'G'
path = a_star(graph, start, goal, h)

if path:
    print("Shortest path from", start, "to", goal, ":", " --> ".join(path))
else:
    print("No path found")