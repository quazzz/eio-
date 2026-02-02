h, w = map(int, input().split())

grid = []
for _ in range(h):
    row = []
    for c in input().strip():
        val = int(c, 16)
        bits = format(val, '04b')
        row.extend(int(b) for b in bits)
    grid.append(row)

height = h
width = len(grid[0])

def yleujutus(sx, sy, mark):
    stack = [(sx, sy)]
    grid[sx][sy] = mark
    while stack:
        x, y = stack.pop()
        for dx, dy in [(0,1),(0,-1), (1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width and grid[nx][ny] == 1:
                grid[nx][ny] = mark
                stack.append((nx, ny))
# ei loe mustaid, mis on klotsi piiril
for i in range(height):
    for j in range(width):
        if grid[i][j] == 1 and (i == 0 or i == height-1 or j == 0 or j == width-1):
            yleujutus(i, j, -1)  


silmaid = 0
for i in range(height):
    for j in range(width):
        if grid[i][j] == 1:
            silmaid += 1
            yleujutus(i, j, -2)

print(silmaid)