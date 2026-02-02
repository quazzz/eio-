
from collections import deque, defaultdict
graph_bfs = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2'],
    '5': ['2'],
    '6': ['3'],
    '7': ['3']
}



def bfs(start, target):
    visited = set()
    q = deque([(start, 0)])
    res = defaultdict(int)
    prev = {}
    visited.add(start)
    while q:
        node, dist = q.popleft()
        res[node] = dist
        if node == target:
            break
        for neighbor in graph_bfs[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                prev[neighbor] = node
                q.append((neighbor, dist + 1))
    return res, prev
distances, prev_nodes = bfs('1', '7')
print("Distances from start:", distances)

# Reconstruct path to target
path = []
cur = '7'
while cur in prev_nodes:
    path.append(cur)
    cur = prev_nodes[cur]
path.append('1')
path.reverse()
print("Shortest path from 1 to 7:", path)       