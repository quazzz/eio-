n = 12033032323323232
copy = n
i = 2
tegurid = []
for index in range(2, int(n ** 0.5) + 2):
    while copy % index == 0:
        tegurid.append(index)
        copy //= index

print(tegurid)