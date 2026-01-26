n = int(input())
s = list(input())
k =0
for i in range(n):
        if s[i] > s[n - i - 1]:
            s[i] = s[n - i - 1]
            k+=1
print(k)
print(''.join(map(str,s)))
