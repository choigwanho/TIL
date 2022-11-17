'''
# [BOJ_1261 알고스팟 -Python3](https://www.acmicpc.net/problem/1261)

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
    distances = [[INF]*M for _ in range(N)]
    distances[x][y]=0
    q = [(0,x,y)]

    while q:
        d,nx,ny = heappop(q)
        if d > distances[nx][ny]:
            continue
        for dx,dy in [(nx-1,ny),(nx+1,ny),(nx,ny-1),(nx,ny+1)]:
            if dx>=N or dx<0 or dy>=M or dy<0:
                continue
            n_d = maze[dx][dy]
            distance = d + n_d
            if distance < distances[dx][dy]:
                distances[dx][dy] = distance
                heappush(q,(distance,dx,dy))
    return distances[N-1][M-1]

import sys
from heapq import heappush, heappop
si = sys.stdin.readline
INF = sys.maxsize

M, N = map(int,si().split())
maze = [list(int(num) for num in str(si().strip())) for _ in range(N)]

print(dijkstra(0,0))