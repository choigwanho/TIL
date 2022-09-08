'''
# [BOJ_2468 안전영역 -Python3](https://www.acmicpc.net/problem/2468)

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

def bfs(y,x,rain):
    q = deque()
    q.append([y,x])
    check[y][x]=1
    while q:
        ny,nx = q.popleft()
        for d in [(-1,0),(1,0),(0,1),(0,-1)]:
            dy,dx=ny+d[0],nx+d[1]
            if 0<=dy<n and 0<=dx<n:
                if graph[dy][dx] >rain and not check[dy][dx]:
                    check[dy][dx]=1
                    q.append([dy,dx])

n = int(si()) # 행과 열의 개수
MAX=0
graph = list()
for i in range(n):
    graph.append(list(map(int,si().split())))
    for j in range(n):
        if graph[i][j] > MAX:
            MAX = graph[i][j]

rst = 0
for rain in range(MAX):
    check = list([0]*n for _ in range(n))
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>rain and not check[i][j]:
                cnt+=1
                bfs(i,j,rain)
    if rst < cnt:
        rst=cnt

print(rst)