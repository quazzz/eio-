from collections import Counter, defaultdict
# loeme osalejate arvu
n = int(input())
mangijad = []
for i in range(n):
    # loeme osaleja i nime ja punktisumma
    s, p = input().split()
    # teisendame punktisumma tekstist arvuks
    p = int(p)
    # TODO: kasutame või salvestame osaleja i andmed
    mangijad.append((s, p))

mangijad.sort(key=lambda x: -x[1])
skoorid = []
i=0
while i < n:
    samad = [mangijad[i][0]]
    skoor = mangijad[i][1]
    j = i + 1
    while j < n and mangijad[j][1] == skoor:
        samad.append(mangijad[j][0])
        j+=1
    alus = i + 1
    lopp = i + len(samad)
    if alus  == lopp:
        sone = f"{alus}."
    else:
        sone = f"{alus}.-{lopp}."
    for nimi in samad:
        skoorid.append(f"{sone} {nimi}")
    i = j
# TODO: koostame ja väljastame vastuse
for rida in skoorid:
    print(rida)

