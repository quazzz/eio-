vaja = int(input())
h1 = int(input())
h2, k2 = map(int,input().split())
h3, k3 = map(int,input().split())
best = float('inf')
for i in range((vaja // k3) + 2):
    for j in range((vaja // k2) + 2):
        tot = i * k3 + j * k2
        if tot >= vaja:
            singles_needed = 0
        else:
            singles_needed = vaja - tot
        tot = i * h3 + j * h2 + h1 * singles_needed
        if tot < best:
            best = tot
print(best)