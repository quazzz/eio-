n,k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

for i in range(n - 3):
    l = i+1
    r = n - 1
    print(f'i: {i} l: {l} r: {r}')
    while l < r:
        summa = nums[i] + nums[l] + nums[r]
        print(summa)
        if summa == k:
            print('JAH')
            exit()
        elif summa < k:
            l+=1
        else:
            r-=1
        
print('EI') 