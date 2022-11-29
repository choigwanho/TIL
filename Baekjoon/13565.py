'''
# [BOJ_13565 침투 -Python3](https://www.acmicpc.net/problem/13565)

## 문제분석
```Python
1. 관찰
- 첫번째 행을 dfs 탐색해서 마지막행에 도달하면 방문, 그헐지 않으면 방문 아님

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

def bfs(r,c):
    visited[r][c]=1
    q = deque()
    q.append((r,c))
    while q:
        nr,nc = q.popleft()
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            dr,dc = nr+d[0],nc+d[1]
            if 0<=dr<m and 0<=dc<n:
                if not visited[dr][dc] and fabric[dr][dc]==0:
                    q.append((dr,dc))
                    visited[dr][dc] = 1

m,n = map(int,si().split())
fabric = list(list(int(i) for i in si().strip()) for _ in range(m))
visited = list(list(0 for _ in range(n)) for _ in range(m))

for i in range(n):
    if not visited[0][i] and fabric[0][i]==0:
        bfs(0,i)

for i in range(n):
    if visited[m-1][i]:
        print('YES')
        break
else:
    print('NO')
