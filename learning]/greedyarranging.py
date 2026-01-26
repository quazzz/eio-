s1 = [
    10,
    10.5,
    11.5,
    12.5
]
s2 = [
    11,
    11.5,
    12.5,
    13.5
]

arr = list(zip(s1, s2))
arr.sort(key= lambda x: x[1])

indexes = []
last = 0

for i, (start,end) in enumerate(arr):
    if start >= last:
        indexes.append(i)
        last = end
print([arr[i] for i in indexes])
