
'''
# [BOJ_1719 택배 -Python3](https://www.acmicpc.net/problem/1719)

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
    time_list = {n:INF for n in path_time}
    node = ['-']*(N+1)
    time_list[start] = 0
    q = []
    heapq.heappush(q,(time_list[start], start))

    while q:
        n_time, n = heapq.heappop(q)
        if time_list[n] < n_time:
            continue
        for nxt, nxt_time in path_time[n]:
            time = n_time + nxt_time
            if time < time_list[nxt]:
                time_list[nxt]=time
                node[nxt]=n
                heapq.heappush(q,(time, nxt))

    return node[1:]

import sys, heapq
from collections import defaultdict
si = sys.stdin.readline
INF = sys.maxsize

N,M = map(int, si().split())
path_time = defaultdict(list)
for _ in range(M):
    a,b,c = map(int,si().split())
    path_time[a].append((b,c))
    path_time[b].append((a,c))

ans = [[] for _ in range(N)]
for i in range(1,N+1):
    for r,v in enumerate(dijkstra(i)):
        ans[r].append(v)

for i in range(N):
    print(*ans[i])

    