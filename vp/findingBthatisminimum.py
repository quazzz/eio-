a,c = map(int,input().split())

def syt(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

if c % a != 0:
    print(-1)
else:
    b = c//a
    if syt(a,b) == 1:
        print(b)
    else:
        print(-1)