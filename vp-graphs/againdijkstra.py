import heapq
graph_dijkstra = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 8},
    'D': {'B': 10, 'C': 3, 'E': 1},
    'E': {'C': 8, 'D': 1}
}

def dijkstra(start, target):
    dist = {node: float('inf') for node in graph_dijkstra}
    dist[start] = 0
    pq = [(0, start)]
    prev = {node: None for node in graph_dijkstra}
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_node == target:
            path = []
            cur = target
            while cur:
                path.append(cur)
                cur = prev[cur]
            path.reverse()
            return path, cur_dist
        if cur_dist > dist[cur_node]:
            continue
        for neighbor, weight in graph_dijkstra[cur_node].items():
            distance = weight + cur_dist
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = cur_node
                heapq.heappush(pq, (distance, neighbor))


prev, dist = dijkstra('A', 'D')
print(prev)