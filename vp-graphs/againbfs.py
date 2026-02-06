
from collections import deque, defaultdict
graph_bfs = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2'],
    '5': ['2'],
    '6': ['3'],
    '7': ['3']
}

visited = set()
q = deque()
q.append('7')
while q:
    el = q.popleft()
    if el == '9':
        print('JAH')
        exit()
    visited.add(el)
    for neighbor in graph_bfs[el]:
        if neighbor not in visited:
            q.append(neighbor)
print('EI')