pos = input()

col = ord(pos[0]) - ord('a')
row = int(pos[1]) - 1

moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

first = []
for dx, dy in moves:
    nx,ny = col +dx, row + dy
    if 0 <= nx <= 8 and 0 <= ny <= 8:
        first.append((nx, ny))
second = set()
for x1, y2 in first:
    for dx, dy in moves:
        nx, ny = x1 + dx, y2 + dy
        if 0 <= nx <= 8 and 0 <= ny <= 8:
            second.add((nx, ny))
tulemus = []
for x1, x2 in second:
    tulemus.append(f"{chr(x1 + ord('a'))}{x2 + 1}")
for x in tulemus:
    print(x)