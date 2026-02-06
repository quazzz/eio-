n = int(input())
teemad = [input() for _ in range(n)]
valitud = input()

length = len(valitud)
vastus = set()
uusvalitud = ''
for i in range(length):
    if valitud[i] != '*':
        uusvalitud += valitud[i]

for teema in teemad:
    if uusvalitud in teema and len(teema) == length:
        vastus.add(teema)
print(len(vastus))
for teema in vastus:
    print(teema)