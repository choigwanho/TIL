'''
# [BOJ_5972 택배 배송 -Python3](https://www.acmicpc.net/problem/5972)

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


def dijkstra(start,target):
    feeds = {n:INF for n in path_feed}
    feeds[start] = 0
    q = []
    heapq.heappush(q,(feeds[start], start))

    while q:
        n_feed, n = heapq.heappop(q)
        if feeds[n] < n_feed:
            continue
        for nxt, nxt_feed in path_feed[n]:
            feed = n_feed + nxt_feed
            if feed < feeds[nxt]:
                feeds[nxt]=feed
                heapq.heappush(q,(feed, nxt))

    return feeds[target]

import sys, heapq
from collections import defaultdict
si = sys.stdin.readline
INF = sys.maxsize

N,M = map(int, si().split())
path_feed = defaultdict(list)
for _ in range(M):
    a,b,c = map(int,si().split())
    path_feed[a].append((b,c))
    path_feed[b].append((a,c))

print(dijkstra(1,N))