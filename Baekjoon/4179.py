'''
dfs로 불과 탈출할 사람의 방문과 이동 거리 비교
'''
import sys
from collections import deque
si = sys.stdin.readline

r, c = map(int, si().split()) # 미로 행의 개수 r, 열의 개수 c
graph = list() # 미로

q_j = deque()
q_f = deque()

visited_j = [[0]*c for _ in range(r)]
visited_f = [[0]*c for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(r):
    row = list(si())
    graph.append(row)
    for j in range(c):
        if row[j] == "J":
            q_j.append((i,j))
            visited_j[i][j] = 1
        elif row[j] == "F":
            q_f.append((i,j))
            visited_f[i][j] = 1

def bfs():
    while q_f:
        x, y = q_f.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited_f[nx][ny] and graph[nx][ny] != "#":
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q_f.append((nx,ny))

    while q_j:
        x, y = q_j.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited_j[nx][ny] and graph[nx][ny] != "#":
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1: # 불과 지훈이의 경로 비교 (방문 or 순서)
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        q_j.append((nx,ny))
            else: # 탈출
                return visited_j[x][y]
    return "IMPOSSIBLE"

print(bfs())
            

            

