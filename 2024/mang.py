from collections import defaultdict
n = int(input())
graph = defaultdict(list)
in_deg = defaultdict(int)
out_deg = defaultdict(int)
for _ in range(n):
    s = input()
    u, v = s[0], s[-1]
    graph[u].append((v, s))
    out_deg[u] += 1
    in_deg[v] += 1

start = None
end = None

for node in set(list(in_deg.keys()) + list(out_deg.keys())):
    out_count = out_deg[node]
    in_count = in_deg[node]
    if out_count - in_count == 1:
        if start is None:
            start = node
        else:
            print('EI')
            exit()
    elif in_count - out_count == 1:
        if end is None:
            end = node
        else:
            print('EI')
            exit()
    elif in_count != out_count:
        print('EI')
        exit()
if start is None:
    start = next((node for node in graph if graph[node]), None)
if start is None:
    print('EI')
    exit()
path = []
def dfs(u):
    while graph[u]:
        v, word = graph[u].pop()
        dfs(v)
        path.append(word)
dfs(start)

if len(path) != n:
    print('EI')
else:
    print('JAH')
    for word in reversed(path):
        print(word)