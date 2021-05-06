import heapq

a=[5,7,9,1,3]

heapq.heapify(a)

print(list(a))

heapq.heappush(a,4)

print(list(a))

heapq.heappop(a)

print(list(a))

print(heapq.nlargest(3,a))

print(heapq.nsmallest(3,a))