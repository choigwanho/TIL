from collections import deque
import sys 
si = sys.stdin.readline

r,c = map(int,si().split()) # 행 r, 열 c
graph = list() # 지도

rq = deque() # 소나기 큐
tq = deque() # 태범이 큐

rmap = list([0]*c for _ in range(r)) # 소나기 맵
tmap = list([0]*c for _ in range(r)) # 태범이 맵

hx,hy = 0,0 # 도착지

for i in range(r):
    row = list(si().strip())
    graph.append(row)
    for j in range(c):
        if row[j] == "H": # 도착지 저장 (태범이의 집)
            hx, hy = i, j
        elif row[j] == "W": # 출발지 태범이 큐에 추가
            tq.append((i, j))
            tmap[i][j] = 1
        elif row[j] == "*": # 소나기 큐에 추가
            rq.append((i,j))
            rmap[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while rq:
        x, y = rq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == "." and rmap[nx][ny] == 0: 
                    rq.append((nx,ny))
                    rmap[nx][ny] = rmap[x][y] + 1

    while tq:
        x, y = tq.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if nx == hx and ny == hy:
                    return tmap[x][y]
                if graph[nx][ny] == "." and tmap[nx][ny] == 0: 
                    if rmap[nx][ny] == 0 or rmap[nx][ny] > tmap[x][y] + 1 : # 소나기는 조건부 판별 (방문, 전파시간)
                        tq.append((nx,ny))
                        tmap[nx][ny] = tmap[x][y] + 1  
    return "FAIL"
    
print(bfs())