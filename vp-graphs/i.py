import heapq
from collections import defaultdict

n, m, start, target = map(int, input().split())
graph = defaultdict(dict)
nodes = set()

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w  
    nodes.add(u)
    nodes.add(v)

def dijkstra(graph, start, target):
    heap = [(0, start)]
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0

    while heap:
        curdist, curnode = heapq.heappop(heap)

        if curnode == target:
            print(curdist)
            return

        if curdist > distances[curnode]:
            continue

        for neighbor, weight in graph.get(curnode, {}).items():
            distance = curdist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))


    print(-1)

dijkstra(graph, start, target)
