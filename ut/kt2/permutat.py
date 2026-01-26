numss = list(map(int,list(input().strip())))
sol = []

def permutate(curComb, mask):
    if len(curComb) == len(numss):
        sol.append(curComb)
        return
    for i in range(len(numss)):
        if not (mask & (1 << i)):
            permutate(curComb + [numss[i]], mask | (1 << i))
permutate([], 0)
for p in sol:
    print(p)
