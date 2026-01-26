def find(j1, j2, i):
    while j1 < j2:
        mid = (j1 + j2) // 2
        print("?", i+1, mid +1, flush=True)
        r = int(input())
        if r == 0:
            j1 = mid + 1
        else:
            j2 = mid
    return j1
def solve(i1,j1,i2,j2):
    if i1 < i2:
        midi= (i1 + i2) // 2
        v[midi] = find(midi, j1, j2)
        solve(i1, midi, j1, v[midi])
        solve(midi + 1, i2, v[midi], j2)

n,m = map(int,input().split())
v = [None] * m
solve(0, m, 0, n)
v = [j+1 if j < n else -1 for j in v]
print('!', *v, flush=True)