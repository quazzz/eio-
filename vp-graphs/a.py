m,n,s = map(int,input().split())
x = None
y = None
arv = 0
suund = None
vasakule = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
}
paremale = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    "W": 'N'
}
dx = {'N': -1, 'S': 1, 'W': 0, 'E': 0}
dy = {'N': 0, 'S': 0, 'W': -1, 'E': 1}
kokku = set()

ruudustik = [[None] * m for _ in range(n)]
for i in range(n):
    line = input()
    for j, taht in enumerate(line):
        ruudustik[i][j] = taht
        if taht in 'NSEW':
            x, y = i, j
            suund = taht
kasud = input().strip()
for kask in kasud:
    if kask == 'V':
        suund = vasakule[suund]
    elif kask == 'P':
        suund = paremale[suund]
    else:
        nx = x + dx[suund]
        ny = y + dy[suund]
        if 0 <= nx < n and 0 <= ny < m and ruudustik[nx][ny] != '#':
            x,y = nx, ny
            if ruudustik[x][y] == '*':
                kokku.add((x,y))
print(len(kokku))
