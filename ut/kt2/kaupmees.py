tulu, kulu = map(int,input().split())
best = float('-inf')
for mask in range(1 << 12): # täielik läbivaatus 2 pow 12 -> 4096
    kuud = []
    tot = 0
    for kuu in range(12):
        if mask & (1 << kuu): # kui väärtuseks on 1, see on hea kuu, kui ei, siis paha kuu
            kuud.append(tulu)
            tot += tulu
        else:
            kuud.append(-kulu)
            tot -= kulu
    valid = True
    for start in range(8): # meil on 8 viiekuist lõiku
        summa = sum(kuud[start:start+5])
        if summa > 0:
            valid = False
            break
    if valid:
        best = max(best, tot)

print(best)

