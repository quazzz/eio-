n = int(input())

nums = list(int(input()) for _ in range(n))
alg = nums[0]
korgus = 0
for i in range(1,n):
    if nums[i] > nums[i-1]:
        continue
    else:
        korgus = max(korgus, nums[i-1] - alg)
        alg = nums[i]
print(korgus)
        
