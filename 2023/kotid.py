k,x,y = map(int,input().split()) 
# k -> auhinnakottide arv
# x -> kui pole kotti, siis liigun too sekunditega
# y -> mitu sek iga kott mineku ajale juurde lisab

dp = [float('inf')] * (k + 1) # how much time we need for i'th
dp[0] = 0 

tagasi = [0] * (k + 1)

for i in range(1, k + 1):
    for j in range(1, i + 1):
        aeg = (2 ** j - 1)
        liikumiseaeg = x + j * y

        if j != i:
            tot += aeg + 2 * liikumiseaeg
        else:
            tot = aeg + liikumiseaeg
        if dp[i - j] + tot < dp[i]:
            dp[i] = dp[i - j] + tot
            tagasi[i] = j
print(dp[k])
moves= []
i=k
while i > 0:
    moves.append(tagasi[i])
    i -= tagasi[i]
print(len(moves))
print(*moves)       


