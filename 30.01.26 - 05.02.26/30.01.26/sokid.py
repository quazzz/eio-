from collections import Counter
n = int(input())
socks = Counter(input() for _ in range(n))
if n % 2 != 0:
    print(-1)
    exit()
need = 0

for key in socks.values():
    if key % 2 != 0:
        need += 1

if need % 2 != 0:
    print(-1)
else:
    print(need // 2)