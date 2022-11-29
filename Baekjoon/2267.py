# [BOJ_2667 단지번호붙이기 - Python3](https://www.acmicpc.net/problem/2667)
'''
### 문제 접근
```Python3
1. 아이디어
- dfs로 단지 방문
- 방문하며 단지 번호 붙이기
- dfs에서 가구수 카운팅

2. 복잡도
- O(V+E) : 5*25*25 >> 가능

3. 자료구조
- 지도: int[][]
- 방문기록: bool[][]
```
'''
### 해결 코드
import sys
input = sys.stdin.readline

N = int(input())

map = [input().strip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dx =[-1,1,0,0]
dy =[0,0,-1,1]

groupCnt = 0
houseCnt =[]

def dfs(y,x):
    visited[y][x] = 1
    houseCnt[groupCnt]+=1
    for i in range(4):
        ny,nx = y + dy[i], x + dx[i]
        if 0<= ny < N and 0<= nx < N:
            if map[ny][nx] == '1' and visited[ny][nx] == 0:
                dfs(ny,nx)

for j in range(N):
    for i in range(N):
        if map[j][i] == '1' and visited[j][i] == 0:
            houseCnt.append(0)
            dfs(j,i)
            groupCnt +=1

print(groupCnt)
houseCnt.sort()
for e in houseCnt:
    print(e)
