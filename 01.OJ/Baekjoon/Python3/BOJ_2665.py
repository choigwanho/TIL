'''
# [BOJ_2665 미로만들기 -Python3](https://www.acmicpc.net/problem/2665)

## 문제분석
```Python
1. 관찰
- n*n 배열
- 검은방, 흰방
- 연결된 흰방 이동 가능
- 검은방을 최소로 바꾸어 끝방에 도착할 수 있도록 함
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
    cnt_black = [[INF for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    visited[x][y] = 1
    cnt_black[x][y] = 0
    q = [(cnt_black[x][y],x,y)]

    while q:
        cnt, vx, vy = heappop(q)

        if [vx, vy] == [n-1,n-1]:
            return  cnt

        if cnt > cnt_black[vx][vy]:
            continue

        for nx, ny in [(vx-1,vy),(vx+1,vy),(vx,vy-1),(vx,vy+1)]:
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    visited[nx][ny]=1
                    if arr[nx][ny]: # 흰칸
                        cnt_black[nx][ny]=cnt
                        heappush(q,(cnt,nx,ny))
                    else: # 검정칸
                        count =  cnt + 1
                        if count < cnt_black[nx][ny]:
                            cnt_black[nx][ny]=count
                            heappush(q,(count,nx,ny))

import sys
from heapq import heappush, heappop
si = sys.stdin.readline
INF = sys.maxsize

n = int(si())
arr = [[int(num) for num in str(si().strip())] for _ in range(n)]

print(dijkstra(0,0))