from collections import defaultdict
n,k = map(int,input().split())
kiirused = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(n):
    korrused = list(map(int, input().split()))
    for i in range(1, n + 1):
        if  len(graph[korrused[i-1]]) == 0:
            graph[korrused[i-1]] = [0]
        else:
            graph[korrused[i-1]].append(korrused[i])
print(graph)

