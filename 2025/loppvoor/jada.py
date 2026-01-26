n,m = map(int,input().split())
# graafi tipp
class Tipp:
    def __init__(self):
        self.vaja = 0
        self.teised = set()

tipud = [Tipp() for _ in range(n)]

for _ in range(m):
    # sisend
    k, *a = map(int,input().split())
    for i in range(k-1):
        u = a[i] - 1 # tipp
        v = a[i + 1] - 1 # järgmine tipp
        if v not in tipud[u].teised: 
            tipud[u].teised.add(v) # lisame järgmist tippu 1. tippu naabrite juurde
            tipud[v].vaja += 1 
stack = []
for i, el in enumerate(tipud):
    if el.vaja == 0:
        stack.append(i)
queue = []
while len(stack) > 0:
    i = stack.pop()
    queue.append(i+1)
    t = tipud[i]
    for muu in t.teised:
        tipud[muu].vaja -= 1
        if tipud[muu].vaja == 0:
            stack.append(muu)
print(' '.join(map(str, queue)))
