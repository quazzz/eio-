from collections import deque, defaultdict

def diff(s1, s2):
    if len(s1) != len(s2):
        return False
    return sum(a != b for a,b in zip(s1, s2)) == 1
n = int(input())
words = [input() for _ in range(n)]
wordfrom, wordto = input().split()

adj = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        if diff(words[i], words[j]):
            adj[words[i]].append(words[j])
            adj[words[j]].append(words[i])
q = deque([(wordfrom, 0)])
visited = set([wordfrom])

while q:
    word, steps = q.popleft()
    if word == wordto:
        print(steps)
        break
    for neighbor in adj[word]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append((neighbor, steps + 1))
