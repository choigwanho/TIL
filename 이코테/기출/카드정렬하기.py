from heapq import heappush, heappop
import sys
si = sys.stdin.readline

n = int(si())

heap = []
for i in range(n):
    heappush(heap, int(si()))

ans = 0

while len(heap) != 1:
    one = heappop(heap)
    two = heappop(heap)
    sum = one + two
    ans += sum
    heappush(heap, sum)

print(ans)
