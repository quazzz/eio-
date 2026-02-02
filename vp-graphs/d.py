from collections import deque
class Tipp:
    def __init__(self):
        self.indeg = 0
        self.teised = set()

n,m = map(int, input().split())
ajad = list(map(int,input().split()))
tipud = [Tipp() for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    tipud[a - 1].teised.add(b - 1)
    tipud[b - 1].indeg += 1

q = deque()
finish = [0] * n

for i, el in enumerate(tipud):
    if el.indeg == 0:
        finish[i] = ajad[i]
        q.append(i)


while q:
    el = q.popleft()
    for other in tipud[el].teised:
        finish[other] = max(finish[other], finish[el] + ajad[other])
        tipud[other].indeg -= 1
        if tipud[other].indeg == 0:
            q.append(other)
print(max(finish))
