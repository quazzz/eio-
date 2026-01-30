from collections import deque, defaultdict

n,m = map(int, input().split())
graph = defaultdict(list)

indeg = [0] * (n+1)

for _ in range(m):
    nums = list(map(int, input().split()))[1:]
    for i in range(len(nums) - 1):
        graph[nums[i]].append(nums[i + 1])
        indeg[nums[i+1]] += 1

q = deque()
for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)
res = []
while q:
    el = q.popleft()
    res.append(el)
    for v in graph[el]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
print(*res)