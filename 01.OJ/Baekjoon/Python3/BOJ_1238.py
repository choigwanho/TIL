'''
# [BOJ_1238 파티 -Python3](https://www.acmicpc.net/problem/1238)

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
    time_info = {town:INF for town in range(1,N+1)}
    time_info[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        t,v = heapq.heappop(q)
        if t > time_info[v]:
            continue
        for n_v, n_t in path_time[v]:
            time = t + n_t
            if time < time_info[n_v]:
                time_info[n_v] = time
                heapq.heappush(q,(time,n_v))
    return time_info

import sys,heapq
from collections import defaultdict
si = sys.stdin.readline
INF = sys.maxsize

N,M,X = map(int,si().split())
path_time = defaultdict(list)
for _ in range(M):
    u,v,w = map(int,si().split())
    path_time[u].append((v,w))


sum_time = dijkstra(X) # 오는시간
for i in range(1,N+1):
    sum_time[i] += dijkstra(i)[X] # 가는시간

print(max(sum_time.values()))