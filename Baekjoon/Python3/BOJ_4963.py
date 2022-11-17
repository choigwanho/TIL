'''
# [BOJ_4963 섬의 개수 -Python3](https://www.acmicpc.net/problem/4963)

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
from collections import deque
import sys
si = sys.stdin.readline 


def bfs(y,x,graph,check):
    q = deque()
    q.append([y,x])
    while q:
        ny, nx= q.popleft()
        for d in xy:
            dy, dx = ny + d[0], nx + d[1]
            if 0 <= dy <h and 0 <= dx < w and not check[dy][dx]:
                if graph[dy][dx]==1:
                    q.append([dy,dx])
                    check[dy][dx]=1

while True:
    w, h = map(int,si().split())

    if w==0 and h==0:
        break

    xy = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]
    ans=0

    graph = list()
    check=list([0 for _ in range(w)] for _ in range(h))

    for _ in range(h):
        graph.append(list(map(int, si().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and not check[i][j]:
                ans+=1
                bfs(i,j,graph,check)
                
    print(ans)
