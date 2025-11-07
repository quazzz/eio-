n = int(input())
osalejad = {}
for _ in range(n):
    osaleja, probleem, aeg, tulemus = input().split()
    osaleja, probleem,aeg = int(osaleja), int(probleem), int(aeg)
    if osaleja not in osalejad:
        osalejad[osaleja] = {}
    if probleem not in osalejad[osaleja]:
        osalejad[osaleja][probleem] = [0,0] 
    if tulemus == 'C':
        if osalejad[osaleja][probleem][1] == 0:
            osalejad[osaleja][probleem][1] = aeg
    elif tulemus == 'I':
        if osalejad[osaleja][probleem][1] == 0:
            osalejad[osaleja][probleem][0] += 1
    
for osaleja in osalejad:
    solved = 0
    total_time = 0
    for probleem in osalejad[osaleja]:
        wrong, correct = osalejad[osaleja][probleem]
        if correct > 0:
            solved += 1
            total_time += correct + wrong * 20
    osalejad[osaleja]['solved'] = solved
    osalejad[osaleja]['time'] = total_time

tulemused = sorted(osalejad.keys(), key=lambda x: (
    -osalejad[x]['solved'],
    osalejad[x]['time'],
    x
))
for osaleja in tulemused:
    print(osaleja, osalejad[osaleja]['solved'], osalejad[osaleja]['time'])
