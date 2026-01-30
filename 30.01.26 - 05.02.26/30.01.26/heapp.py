import heapq

arr = [5,4,3,2,1]
heapq.heapify(arr)
print(arr)

heapq.heappop(arr)
print(arr)
c = heapq.nlargest(2, arr)
print(c)