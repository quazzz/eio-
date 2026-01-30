w = list(input())

l, r = 0, len(w) - 1
k = 0
while l < r:
    if w[l] < w[r]:
        w[l] = w[r]
        k += 1
    l += 1
    r -= 1
print(k)
print(*w)