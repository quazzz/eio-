from collections import deque, defaultdict
n,m = map(int,input().split())
graph = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

color = [None] * n


def bfs(index):
    q = deque()
    q.append(index)
    color[index] = True

    while q:
        el = q.popleft()
        for neighbor in graph[el]:
            if color[neighbor] is None:
                color[neighbor] = not color[el]
                q.append(neighbor)
            else:
                if color[neighbor] == color[el]:
                    print('EI')
                    exit()
for i in range(n):
    if color[i] is None:
        bfs(i)

print('JAH')

