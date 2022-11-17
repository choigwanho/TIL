'''
# [BOJ_14503 로봇 청소기 -Python3](https://www.acmicpc.net/problem/14503)

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


left = [(-1,0),(0,-1),(1,0),(0,1)]

def bfs(sx, sy, dir):
    cleaned[sy][sx] = 1
    q = deque([sx, sy, dir])
    while q:
        nx, ny, ndir = q.popleft()
        dx, dy = nx + left[ndir], ny + left[ndir]
        if 0 <= dx < m and 0 <= dy < n:
            if not cleaned[dy][dx] and graph[dy][dx]: # 왼쪽 방향에 아직 청소하지 않은 공간이 존재           
                cleaned[dy][dx] = 1
                if ndir-1<0:
                    q.append([dx,dy,3])
                else:
                    q.append([dx,dy,ndir-1])
        else: # 왼쪽 방향에 청소할 공간이 없음
            if ndir-1<0:
                q.append([nx,ny,3])
            else:
                q.append([nx,ny,ndir-1])




        if ndir == 0:
            
            
        if ndir == 1:

        if ndir == 2:

        if ndir == 3:

            dx, dy = nx + d[0], ny + d[1]
            if 0 <= dx < m and 0 <= dy < n and not cleaned[dy][dx]:
                if :
                    cleaned[dy][dx] = 1
                    q.append([dx,dy])

n,m = map(int,si().split())
r,c,d = map(int,si().split())
graph = list(list(map(int,si().split())) for _ in range(n))
cleaned = list(list(0 for _ in range(m)) for _ in range(n))

bfs(r,c,d)


