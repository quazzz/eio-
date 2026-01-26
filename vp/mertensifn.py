def solve(n):
    values = [1] * (n + 1)
    is_prime = [True] * (n+1)
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i, n+1,i):
                is_prime[j]= False
                values[j] *= -1
            for j in range(i*i, n+1, i*i):
                values[j] = 0
    m = 0
    for k in range(1, n+1):
        m+=values[k]
    return m

n = int(input())
print(solve(n))