#bfs algorithm
from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    print("BFS traversal starting from node",start,end=":")
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph={
    0:[1,2],
    1:[0,3],
    2:[0,4],
    3:[1],
    4:[2]
}
start_node=0
bfs(graph,start_node)
