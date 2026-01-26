P = int(input())
H1 = int(input())
H2, K2 = (int(x) for x in input().split())
H3, K3 = (int(x) for x in input().split())

minmaalne = float('inf')

for large in range((P // K3) + 2):
    for small in range((P // K2) + 2):
        candies = large * K3 + small * K2
        if candies >= P:
            singles_needed = 0
        else:
            singles_needed = P - candies
        tot = large * H3 + small * H2 + singles_needed * H1
        if tot < minmaalne:
            minmaalne = tot
print(minmaalne)