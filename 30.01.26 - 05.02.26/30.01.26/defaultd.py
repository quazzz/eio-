from collections import defaultdict, deque
import sys
graph = defaultdict(list)
n,m =  map(int,sys.stdin.readline().strip().split())
indeg = [0] * (n + 1)
for _ in range(m):
    nums = list(map(int, sys.stdin.readline().strip().split()))[1:]
    for i in range(len(nums) - 1):
        indeg[nums[i + 1]] += 1
        graph[nums[i]].append(nums[i + 1])

q = deque()
for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)

vastus = []

while q:
    el = q.popleft()
    vastus.append(el)
    for other in graph[el]:
        indeg[other] -=  1
        if indeg[other] == 0:
            q.append(other)

print(*vastus)
