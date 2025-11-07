s,n = map(int,input().split())
liidetavad = sorted(list(map(int,input().split())), reverse=True)
combinations = []
def backtrack(idx, cursum, curcomb):
    if cursum == s:
        combinations.append(curcomb)
    if cursum > s or idx == n:
        return
    for i in range(idx, n):
        if i > idx and liidetavad[i] == liidetavad[i - 1]:
            continue
        backtrack(i + 1, liidetavad[i] + cursum, curcomb + [liidetavad[i]])

backtrack(0, 0, [])
for comb in combinations:
    print(''.join(map(str,comb)))