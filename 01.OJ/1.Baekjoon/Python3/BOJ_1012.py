# [BOJ_1012 유기농 배추 - Python3](https://www.acmicpc.net/problem/1012)
'''
### 문제 접근
```
1. 아이디어
- BFS로 그룹 탐색
2. 복잡도
- O(V+E) : (50*50 + 4*50*50)T  >> 가능
3. 자료구조
- gragh: int[][]
- visited: bool[][]
```
'''
### 해결 코드
from collections import deque
import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    m, n, k = map(int, input().strip().split()) # 배추밭의 가로, 세로, 배추가 심어져 있는 위치의 개수

    farm = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().strip().split())
        farm[y][x] = 1

    visited = [[False]*m for _ in range(n)]
    answer = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs(y,x):
        q = deque()
        q.append([y,x])

        while q:
            y, x = q.popleft()
            visited[y][x] = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<= nx <m and 0<= ny <n:
                    if farm[ny][nx] == 1 and visited[ny][nx] == False:
                        visited[ny][nx] = True
                        q.append([ny,nx])

    for j in range(n):
        for i in range(m):
            if farm[j][i] == 1 and visited[j][i] == False:
                visited[j][i] = True
                bfs(j,i)
                answer +=1

    print(answer)