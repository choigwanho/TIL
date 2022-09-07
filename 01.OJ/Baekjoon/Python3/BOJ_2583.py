'''
# [BOJ_2583 영역 구하기 -Python3](https://www.acmicpc.net/problem/2583)

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

def bfs(y,x):
    temp=0
    q = deque()
    q.append([y,x])
    while q:
        temp +=1
        ny, nx = q.popleft()
        for d in [(-1,0),(1,0),(0,1),(0,-1)]:
            dy,dx = ny +d[0], nx + d[1]
            if 0 <= dy <m and 0 <= dx <n:
                if graph[dy][dx]:
                    q.append([dy,dx])
                    graph[dy][dx]=0

    ans_list.append(temp)

m,n,k = map(int,si().split())
graph = list([1]*n for _ in range(m))
for _ in range(k):
    x1,y1,x2,y2 = map(int,si().split())
    for i in range(m):
        for j in range(n):
            if y1 <= i < y2 and x1 <= j < x2:
                graph[i][j]=0

cnt = 0
ans_list = list()

for i in range(m):
    for j in range(n):
        if graph[i][j]:
            graph[i][j]=0
            cnt += 1
            bfs(i,j)
ans_list.sort()
print(cnt)
print(*ans_list)

            