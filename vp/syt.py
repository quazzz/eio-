def syt(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def syt2(a,b):
    return a if b == 0 else syt(b,  a % b)

def vyk(a,b):
    temp = syt2(a,b)
    return (a / temp * b) if temp else 0
