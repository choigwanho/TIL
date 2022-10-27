'''
# [BOJ_1916 최소비용 구하기 -Python3](https://www.acmicpc.net/problem/1916)

## 문제분석
```Python
1. 관찰
-

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
def dijkstra(start):
    w_info = {bus_stop:INF for bus_stop in range(N+1)}
    
    w_info[start]=0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        w,v = heapq.heappop(q)
        if w > w_info[v]:
            continue
        for n_v, n_w in bus_info[v]:
            cost = w + n_w
            if cost < w_info[n_v]:
                w_info[n_v] = cost
                heapq.heappush(q,(cost,n_v))
    return w_info

import sys, heapq
from collections import defaultdict
si = sys.stdin.readline
INF = sys.maxsize

N = int(si())
M = int(si())
bus_info = defaultdict(list)
for _ in range(M):
    u,v,w = map(int,si().split())
    bus_info[u].append((v,w))

S,E = map(int,si().split())

print(dijkstra(S)[E])