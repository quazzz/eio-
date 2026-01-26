def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

n = int(input())
kaitsjad = [tuple(map(int, input().split())) for _ in range(n)]
rundaja = tuple(map(int, input().split()))
varav = tuple(map(int, input().split()))

kaitse_varaval = sum(1 for k in kaitsjad if cross_product(rundaja, varav, k) * cross_product(rundaja, varav, varav) >= 0 and cross_product(rundaja, varav, k) == 0)
if kaitse_varaval <= 1:
    print("JAH")
    exit()

for kaitsja in kaitsjad:
    cp_varav = cross_product(rundaja, kaitsja, varav)
    kaitse_pool = sum(1 for k in kaitsjad if cross_product(rundaja, kaitsja, k) * cp_varav >= 0)
    if kaitse_pool <= 1:
        print("JAH")
        exit()

print("EI")