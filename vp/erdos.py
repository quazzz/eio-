from collections import deque, defaultdict
n = int(input())
papers = []
authorsSet = set()
for _ in range(n):
    s = input()
    authorPart, title = s.rsplit(';', maxsplit=1)
    authors = [x.strip() for x in authorPart.split(';')]
    papers.append(authors)
    authorsSet.update(authors)

erdos = {'Erdos, Paul': 0}

coauthors = defaultdict(set)
for authors in papers:
    for a in authors:
        for b in authors:
            if a != b:
                coauthors[a].add(b)
queue = deque(['Erdos, Paul'])
while queue:
    cur = queue.popleft()
    curNum = erdos[cur]
    for neighbor in coauthors[cur]:
        if neighbor not in erdos:
            erdos[neighbor] = curNum + 1
            queue.append(neighbor)
res = []
for author in sorted(authorsSet):
    if author != 'Erdos, Paul':
        num = erdos.get(author, -1)
        res.append(f"{author} {num}")
print('\n'.join(res))