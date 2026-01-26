a, b = map(int, input().split('/'))
c, d = map(int, input().split('/'))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

lcms = lcm(b, d)
firstexp = a * (lcms // b)
secondexp = c * (lcms // d)

arv = firstexp - secondexp

gcds = gcd(abs(arv), lcms)
arv //= gcds
lcms //= gcds

divider = abs(arv) // lcms if abs(arv) // lcms > 1 else '-0'
frac_num = abs(arv) % lcms
frac_den = lcms

print(divider if arv > 0 else -divider)
print(f"{frac_num}/{frac_den}")