n = int(input())
koned = list(map(int,input().split()))

def survives(start, koned):
    c = start
    for kone in koned:
        if kone > c:
            return False
        if kone == c:
            c -=1
    return True
lo = 1
high = max(koned) + n

while lo < high:
    mid = (lo + high) // 2
    if survives(mid, koned):
        high = mid 
    else:
        lo = mid + 1
print(lo)