'''
# [BOJ_11779 최소비용 구하기 2 -Python3](https://www.acmicpc.net/problem/11779)

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
    time_list = [INF]*(n+1)
    visited = []
    time_list[start] = 0
    q = [(time_list[start], start)]

    while q:
        n_time, n_v = heappop(q)
        if time_list[n_v] < n_time:
            continue
        for nxt_v, nxt_time in path_cost[n_v]:
            time = n_time + nxt_time
            if time < time_list[nxt_v]:
                time_list[nxt_v]=time
                visited.append(n_v)
                heappush(q,(time, nxt_v))

    return (time_list,visited)

import sys
from heapq import heappush, heappop
si = sys.stdin.readline
INF = sys.maxsize

n = int(si())
m = int(si())
path_cost = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,si().split())
    path_cost[a].append((b,c))

s,e = map(int,si().split())
cost_list, city_list = dijkstra(s)
print(cost_list[e])
print(len(city_list))
print(*city_list)