'''
# [BOJ_1504 특정한 최단 경로 -Python3](https://www.acmicpc.net/problem/1504)

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
    distances = [INF]*(N+1)
    distances[start]=0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        d,v = heapq.heappop(q)
        if d > distances[v]:
            continue
        for n_v, n_d in info[v]:
            distance = d + n_d
            if distance < distances[n_v]:
                distances[n_v] = distance
                heapq.heappush(q,(distance,n_v))
    return distances

import sys,heapq
si = sys.stdin.readline
INF = 0xffffff

N, E = map(int,si().split())
info = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,si().split())
    info[a].append((b,c))
    info[b].append((a,c))

V1,V2 = map(int,si().split())

case_1 = dijkstra(1)[V1] + dijkstra(V1)[V2] + dijkstra(V2)[N]
case_2 = dijkstra(1)[V2] + dijkstra(V2)[V1] + dijkstra(V1)[N]

if case_1 >= INF and case_2 >= INF:
    print(-1)
else:
    print(min(case_1,case_2))
