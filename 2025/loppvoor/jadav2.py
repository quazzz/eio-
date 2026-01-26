n,m = map(int,input().split())
class Tipp:
    def __init__(self):
        self.teised = set()
        self.vaja = 0
tipud = [Tipp() for _ in range(n)]

for _ in range(m):
    k, *nums = map(int,input().split())
    for i in range(k-1):
        u = nums[i] - 1
        v = nums[i + 1] - 1
        if v not in tipud[u].teised:
            tipud[u].teised.add(v)
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
            queue.append(muu)
print(''.join(map(str, queue)))