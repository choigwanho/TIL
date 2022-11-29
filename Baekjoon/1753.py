'''
# [BOJ_1753 최단경로 -Python3](https://www.acmicpc.net/problem/1753)

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
    w_dic = {n:INF for n in range(V+1)}
    w_dic[start] = 0
    q = []
    heapq.heappush(q,(w_dic[start], start))
    while q:
        n_w, n = heapq.heappop(q)
        if w_dic[n] < n_w:
            continue
        for nxt, nxt_w in path_w[n]:
            w = n_w + nxt_w
            if w < w_dic[nxt]:
                w_dic[nxt]=w
                heapq.heappush(q,(w, nxt))
    return w_dic

import sys, heapq
si = sys.stdin.readline
INF = sys.maxsize

V,E = map(int, si().split())
K = int(si())
path_w = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,si().split())
    path_w[u].append((v,w))

ans = dijkstra(K)
for i in range(1,V+1):
    if i==K:
        print(0)
    elif ans[i]==INF:
        print('INF')
    else:
        print(ans[i])