nums = list(map(int,input().split()))
s = ''.join(map(str, nums))
if s[::-1] == s:
    print('JAH')
    print(*nums)
else:
    l,r = 0, len(nums) - 1
    changes = 0
    while l<=r:
        if nums[l] != nums[r]:
            nums[r] = nums[l]
            changes += 1
            if changes > 1:
                print('EI')
                exit()
        l+=1
        r-=1
    if nums[::-1] == nums:
        print('JAH')
        print(*nums)
    else:
        print('EI')

