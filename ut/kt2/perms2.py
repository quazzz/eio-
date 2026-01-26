numss = list(map(int,input().strip()))
sol = []
used = [False] * len(numss)

def permutate(curComb):
    if len(curComb)== len(numss):
        sol.append(curComb[:])
        return
    for i in range(len(numss)):
        if not used[i]:
            used[i ] = True
            curComb.append(numss[i])
            permutate(curComb)
            curComb.pop()
            used[i] = False
permutate([])
for p in sol:
    print(p)