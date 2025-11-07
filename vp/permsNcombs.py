mask = 0 
# permutatsioone on kokku N!, kiir lahendus
n = list(map(int,input().split()))
vastus = []
def permutations(curComb, mask):
    if len(curComb) == len(n):
        vastus.append(curComb)
        return
    for i in range(len(n)):
        if not mask & (1 << i):
            permutations(curComb + [n[i]], mask | ( 1 << i))

permutations([], mask)

length = int(input())
arr = list(map(int,input().split()))
vastus2 = []
def combinations(idx, curComb):
    if len(curComb) == length:
        vastus2.append(curComb)
        return
    if idx == len(arr):
        return 
    combinations(idx + 1, curComb + [arr[idx]])
    combinations(idx + 1, curComb)
combinations(0, [])
print(vastus2)