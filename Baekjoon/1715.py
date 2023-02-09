from heapq import heappush, heappop
import sys
si = sys.stdin.readline

n = int(si()) # 비교 횟수, 1e5

card = list()
for _ in range(n):
    heappush(card, int(si())) # O(logn)

ans = 0
while len(card) > 1: # O(nlogn)
    c1 = heappop(card)
    c2 = heappop(card)
    ans += (c1+c2)
    heappush(card, c1+c2) # 더한 조합 넣기!!
print(ans)