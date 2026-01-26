n = int(input())
nums = sorted(input())
arr = []
for char in nums:
    arr.append(int(char))

a = ''
b = ''

for i in range(n):
    if i % 2 == 0:
        a += nums[i]
    else:
        b += nums[i]

new_1 = int(''.join(a))
new_2 = int(''.join(b))

print(new_1 + new_2)