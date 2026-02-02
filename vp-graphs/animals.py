from collections import defaultdict
n = int(input())

graph = defaultdict(list)
indeg = defaultdict(int)
for _ in range(n):
    a,b = map(str, input().split())
    graph[a].append(b)
    indeg[b] += 1
    if a not in indeg:
        indeg[a] = 0
stack = []

for k,v in indeg.items():
    if v == 0:
        stack.append(k)
vastus = []
while stack:
    el = stack.pop()
    vastus.append(el)
    for other in graph[el]:
        indeg[other] -= 1
        if indeg[other] == 0:
            stack.append(other)
print(vastus)