
# tund hiljem tuli mõte kuidas võiks
# eurid sentideks
# lihtsalt ymardan koik hinnad, siis sum() neid, current võtega teen 
# moned testid paaseb ikka veel 

n = int(input())
ostud = []
for _ in range(n):
    toode = input().split()
    nimi = toode[0]
    euri, senti = int(toode[1]), int(toode[2])
    ostud.append((nimi, euri * 100 + senti))

def ymarda(senti):
    r = senti % 5
    if r in (1,2,6,7):
        return senti - r # nt senti = 12 -> 12 % 5 = 2 -> 12 - 2 = 10 -> ymardatud --> liigsed sendid maha 
    elif r in (3,4,8,9):
        return senti + (5 - r) # nt senti = 13, r on siis 3, 13 + (5 - 3) = 15 --> liigsed sendid juurde
    else:
        return senti
tooted = []
curSum = 0
curToode = []
for nimi, senti in ostud:
    curToode.append((nimi, senti))
    curSum += senti
    if curSum % 5 == 0:
        tooted.append(curToode)
        curToode = []
        curSum = 0
if curToode: # jäi veel
    tooted.append(curToode)
tot = sum(ymarda(senti) for toode in tooted for _, senti in toode)
euri = tot // 100
senti = tot % 100
print(euri, senti)
for toode in tooted:
    print(''.join(nimi for nimi,_ in toode))