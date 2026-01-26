n = int(input())

# TODO: leiame vastuse
vastus = []

for i in range(1,n+1):
    vastus.append(i * (n - i + 1))

for vas in vastus:
    print(vas)