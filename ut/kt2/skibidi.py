from collections import Counter

n = int(input())
nums = Counter([map(int,input().split()) for _ in range(n)])
counter = 0
for _,v in nums.items():
    if v % 2 != 0:
        counter += 1

if counter % 2 != 0:
    print(-1)
else:
    print(counter // 2)