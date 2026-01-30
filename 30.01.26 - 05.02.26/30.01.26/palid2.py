w = list(input())

for i in range(len(w) // 2):
    if w[i] < w[len(w) - i - 1]:
        w[i] = w[len(w) - i - 1]
print(*w)