'''
# [BOJ_1446 지름길 -Python3](https://www.acmicpc.net/problem/1446)

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
    distances = {node:int(1e9) for node in dis_dic}
    distances[start] = 0
    q = []
    heapq.heappush(q,[distances[start],start])

    while q:
        cur_dis, cur_v = heapq.heappop(q)
            
        for new_v, new_dis in dis_dic[cur_v]:
            distance = cur_dis + new_dis
            if distance < distances[new_v]:
                distances[new_v] = distance
                heapq.heappush(q,[distance,new_v])

    return distances


import sys, heapq
from collections import defaultdict
si = sys.stdin.readline

n, d = map(int,si().split()) # e, total_dis

dis_dic = defaultdict(list)
for _ in range(n):
    v1,v2,dis = map(int,si().split())
    dis_dic[v1].append((v2,dis))
    dis_dic[v2].append((v1,dis))

