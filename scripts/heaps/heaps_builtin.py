"""
Note this only allows for min heaps
"""
import heapq

heap = [4, 7, 3, -2, 1, 0]
heapq.heapify(heap)

print(heap)

nums = [4, 7, 3, -2, 1, 0]
heap_str = []

for num in nums:
    heapq.heappush(heap_str, num)

while heap_str:
    print(heapq.heappop(heap_str))
