t,w,n = map(int,input().split())
vaasid = []
for _ in range(n):
    suk, vaa = map(int,input().split())
    aeg = 3 * w * suk
    vaasid.append((suk, vaa, aeg))

dp = [[0] * (t+1) for _ in range(n+1)]
votta = [[False] * (t+1) for _ in range(n+1)]
for i in range(1, n+1):
    suk, vaa, aeg = vaasid[i-1]
    for j in range(t + 1):
        dp[i][j] = dp[i-1][j]
        votta[i][j] = False
        if j >= aeg:
            vaaVoetud = dp[i-1][j-aeg] + vaa
            if vaaVoetud > dp[i][j]:
                dp[i][j] = vaaVoetud
                votta[i][j] = True
voetud = []
j = t
for i in range(n, 0, -1):
    if votta[i][j]:
        suk, vaa, aeg = vaasid[i-1]
        voetud.append([suk, vaa])
        j -= aeg
voetud.reverse()
for vaas in voetud:
    print(*vaas)
     