n = int(input())
countries = [input() for _ in range(n)]
m = int(input())

osalejad = {c: (0,0,0,0,0) for c in countries}

for _ in range(m):
    match,score = input().split()
    s1,s2 = map(int,score.split(':'))
    t1,t2 = match.split('-')

    p1, w1, diff1, gd1, g1 = osalejad[t1]
    p2,w2,diff2,gd2,g2 = osalejad[t2]
    g1+=1
    g2+=1
    gd1 += s1
    gd2 += s2
    diff1 += s1 -s2
    diff2 += s2 - s1
    if s1 > s2:
        p1 += 3
        w1 += 1
    elif s1 < s2:
        p2 += 3
        w2 += 1
    else:
        p1 += 1
        p2 += 1
    osalejad[t1] = (p1,w1,diff1,gd1,g1)
    osalejad[t2] = (p2,w2,diff2,gd2,g2)

tulemus = sorted(osalejad, key=lambda x: (
    -osalejad[x][0],
    -osalejad[x][1],
    -osalejad[x][2],
    -osalejad[x][3],
    osalejad[x][4],
    x.lower()
))
print(*tulemus, sep='\n')