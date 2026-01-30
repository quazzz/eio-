from collections import defaultdict

graph = defaultdict(list)

nums = [1,2,3,4,5]

for i in range(len(nums) -1):
    graph[nums[i]].append(nums[i+1])

print(graph)