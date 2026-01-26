def leiapikim(n, s):
    pikkused = [1] * n
    indeksid = [None] * n
    for i in range(n):
        indeksid[i] = i
    pikim = 0
    pikimaindeks = 0
    for i in range(n):
        if(pikkused[i] > pikim):
            pikim = pikkused[i]
            pikimaindeks = i
        for j in range(i+1, n):
            if(s[j] > s[i] and pikkused[i] + 1 > pikkused[j]):
                pikkused[j] = pikkused[i] + 1
                indeksid[j] = i
    osajada = [None] * pikim
    for i in range(pikim, 0, -1):
        osajada[i-1] = s[pikimaindeks]
        pikimaindeks = indeksid[pikimaindeks]
    return osajada
print(leiapikim(5, [5,4,2,3,5]))
 
