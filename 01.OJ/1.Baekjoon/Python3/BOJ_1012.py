# [BOJ_1012 유기농 배추 - Python3](https://www.acmicpc.net/problem/1012)
'''
### 문제 접근
1. 아이디어
-
2. 복잡도
-
3. 자료구조
-
'''
### 해결 코드
import sys
input = sys.stdin.readline



t = int(input())    # 테스트 케이스의 개수
m, n, k = map(int, input().split()) # 배추밭의 가로, 세로, 배추가 심어져 있는 위치의 개수

farm = [[0]*m for _ in range(n)]
answer = 0

for _ in range(k):
    x, y = map(int, input().split())
    farm[y][x] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 배추가 심어져 있으면 dfs하여 그룹 탐색
def dfs(x,y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<= nx <n and 0<= ny <m:    # 배추밭의 범위내에 있고
            if farm[nx][ny] == 1:    # 배추가 심어저 있으면


for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            dfs(i,j)
            answer +=1

print(answer)

















