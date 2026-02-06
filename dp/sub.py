nums = list(map(int,input().split()))
n = len(nums)
cur_max = nums[0]
global_max = nums[0]

for i in range(1, n):
    cur_max = max(nums[i], cur_max + nums[i])
    if cur_max > global_max:
        global_max = cur_max
print(global_max)