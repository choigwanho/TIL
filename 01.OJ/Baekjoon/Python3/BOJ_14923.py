'''
# [BOJ_14923 미로 탈출 -Python3](https://www.acmicpc.net/problem/14923)

## 문제분석
```Python
1. 관찰
- 요술을 한 번 사용할 수 있고 있을 때와 없을 때를 순차적으로 비교하면서 이동하여 확인

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
def bfs():
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[HX-1][HY-1][1]=1

    q = deque([(HX-1,HY-1,1,0)])

    while q:
        x,y,magic,cnt= q.popleft()

        if x==EX-1 and y==EY-1:
            return cnt

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if visited[nx][ny][magic]==1:
                continue
            if magic and matrix[nx][ny]==1: # 벽허물고 이동
                visited[nx][ny][0] = 1
                q.append((nx,ny,0,cnt+1))
            if matrix[nx][ny]==0: # 그냥 이동
                visited[nx][ny][magic] = 1
                q.append((nx,ny,magic,cnt+1))

    return -1

import sys
from collections import deque
si = sys.stdin.readline

N,M = map(int,si().split())
HX,HY = map(int,si().split())
EX,EY = map(int,si().split())
matrix = [list(map(int,si().split())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs())