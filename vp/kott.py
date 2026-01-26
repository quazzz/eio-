tootede_arv = int(input())
tooted = {}

# loeme tooteid ja nende hindu
for _ in range(tootede_arv):
    toode = input()
    hind = int(input())
    tooted[toode] = hind

# loeme soovi
soovide_arv = int(input())
soovid = [input() for _ in range(soovide_arv)]

# leiame soovide hindu
hinnad = [tooted[soov] for soov in soovid]

# leiame maksimaalse toote hinna ja selle indeksi
kõrgeim_hind = max(hinnad)
kõrgeima_hinna_asukoht = hinnad.index(kõrgeim_hind)

# leiame minimaalse toote hinna ja selle nimetuse
odavaim_hind = min(tooted)
odavaim_toode = min(tooted, key= tooted.get)

# kui odavaima hind on väiksem kui kõrgeima
if odavaim_hind < kõrgeim_hind:
    # lihtsalt swappime hinnasid omavahel ära
    tooted[soovid[kõrgeima_hinna_asukoht]], tooted[odavaim_toode] = tooted[odavaim_toode], tooted[soovid[kõrgeima_hinna_asukoht]]

kokku = sum(tooted[soov] for soov in soovid)
print(kokku)