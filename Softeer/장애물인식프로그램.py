from collections import deque
import sys
si = sys.stdin.readline

def bfs(a,b,):
    cnt = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(a,b)])
    graph[a][b] = "0"
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == "1":
                    graph[nx][ny] = "0"
                    cnt += 1
                    q.append((nx,ny))
    return cnt

n = int(si()) # 지도의 크기 n
graph = list(list(si().strip()) for _ in range(n)) # 지도, 장애물 1 도로 0

cnt = 0 # 구역의 수
p = list() # 각 구역에서의 장애물 개수
for i in range(n):
    for j in range(n):
        if graph[i][j] == "1":
            cnt +=1
            p.append(bfs(i,j))

p.sort()

print(cnt)
for i in range(cnt):
    print(p[i]) 