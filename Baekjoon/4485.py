'''
# [BOJ_4485 녹색 옷 입은 애가 젤다지? -Python3](https://www.acmicpc.net/problem/4485)

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
def dijkstra(x,y):
    rupees = [[INF]*N for _ in range(N)]
    rupees[x][y]= graph[x][y]
    q = [(rupees[x][y],x,y)]

    while q:
        r,nx,ny = heappop(q)
        if r > rupees[nx][ny]:
            continue
        for dx,dy in [(nx-1,ny),(nx+1,ny),(nx,ny-1),(nx,ny+1)]:
            if dx>=N or dx<0 or dy>=N or dy<0:
                continue
            n_r = graph[dx][dy]
            rupee = r + n_r
            if rupee < rupees[dx][dy]:
                rupees[dx][dy] = rupee
                heappush(q,(rupee,dx,dy))
    return rupees[N-1][N-1]

import sys
from heapq import heappush, heappop
si = sys.stdin.readline
INF = sys.maxsize

t = 1
while True:
    N = int(si())
    if N ==0:
        exit(0)

    graph = [list(map(int,si().split())) for _ in range(N)]

    ans = dijkstra(0,0)

    print(f'Problem {t}: {ans}')
    t+=1