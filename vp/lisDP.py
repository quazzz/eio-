def leiapikimpikkus(n, jada):
    pikkused = [1] * n
    vastus = 0
    for i in range(n):
        vastus = max(vastus, pikkused[i])
        for j in range(i+1,n):
            if jada[j] > jada[i]:
                pikkused[j] = max(pikkused[j], pikkused[i+1])
    return pikkused
print(leiapikimpikkus(5, [5,4,2,3,1]))