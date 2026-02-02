from heapq import heappop, heappush
graph_dijkstra = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}
n = len(graph_dijkstra)

def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    prev = {node: None for node in graph}
    while heap:
        curdist, curnode = heappop(heap)
        if curdist > distances[curnode]:
            continue
        for neighbor, weight in graph[curnode].items():
            distance = curdist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = curnode
                heappush(heap, (distance, neighbor))
    return distances, prev
graph_dijkstra = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

distances, previous = dijkstra(graph_dijkstra, 'A')
print("Shortest distances:", distances)
print("Previous nodes:", previous)