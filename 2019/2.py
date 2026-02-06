from collections import deque
n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]
sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            sx,sy = i, j

deltad = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * m for _ in range(n)]
parent = [[None] * m for _ in range(n)]
def isExit(x, y):
    return grid[x][y] == '.' and (x == 0 or x == n - 1 or y == 0 or y == m-1)
    

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy, 0))
    visited[sx][sy] = True

    while q:
        x,y, dist = q.popleft()
        if isExit(x, y):
            path_x, path_y = x, y
            while (path_x, path_y) != (sx, sy):
                grid[path_x][path_y] = '*'
                path_x, path_y = parent[path_x][path_y]
            return dist
        for dx, dy in deltad:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and not visited[nx][ny]:
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = True
                parent[nx][ny] = (x,y)
    return -1


minimal_dist = bfs(sx, sy)
print(minimal_dist)
for row in grid:
    print(''.join(row))