'''
# [BOJ_10282 해킹 -Python3](https://www.acmicpc.net/problem/10282)

## 문제분석
```Python
1. 관찰
- 의존관계 컴퓨터끼리는 감염됨
- 

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
def sol(n,d,c,network):
    times = [INF for _ in range(n+1)]
    times[c] = 0
    q = [(times[c],c)]
    last_time = 0
    c_list = []
    while q:
        t,v = heappop(q)
        if t > times[v]:
            continue
        last_time = t
        c_list.append(v)
        for n_v, n_t in network[v]:
            time = t+n_t
            if time < times[n_v]:
                times[n_v]=time
                heappush(q,(time,n_v))
                
    return [len(c_list),last_time]

import sys
from heapq import heappush, heappop
si = sys.stdin.readline
INF = sys.maxsize

T = int(si()) # tc 개수
for _ in range(T):
    n,d,c = map(int,si().split()) # 컴퓨터의 개수(node), 의존성 개수(edge), 해킹당한 컴퓨터의 번호(start_node)
    network = [[] for _ in range(n+1)]  
    for _ in range(d):
        a,b,s = map(int,si().split())
        network[b].append((a,s))
    print(*sol(n,d,c,network))