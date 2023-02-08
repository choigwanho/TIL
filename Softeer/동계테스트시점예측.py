'''
바깥 공기를 기준으로 얼음에 접근하는 횟수가 2회 이상이 되도록 얼음을 다 녹일때까지 반복
'''


import sys
from collections import deque
si = sys.stdin.readline

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[0, 0]])
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if 0 <= nx < n and 0 <= ny < m:
                # 탐색하는 곳이 얼음이면 방문 여부 카운트
                if graph[nx][ny] == 1:
                    visited[nx][ny] += 1

                # 얼음이 아니고 탐색하지 않았다면 탐색
                elif visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

    # 한시간이 지나면 얼음을 2번 이상 방문한 곳을 녹인다.
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                graph[i][j] = 0


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
cnt = 0

# 모든 얼음이 녹을 때까지 반복한다.
while True:
    # 모든 얼음이 녹았다면 반복을 멈춘다.
    if graph.count(graph[0]) == n:
        break
    
    visited = [[0] * m for _ in range(n)] # 탐색 여부
    bfs() # bfs 탐색
    cnt += 1 # 시간 카운트

print(cnt)
