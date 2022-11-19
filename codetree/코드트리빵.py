import sys
from collections import deque
si = sys.stdin.readline

def OOB(x,y):
    return x<0 or x>=N or y<0 or y>=N

# 가장 가까운 베이스캠프를 리턴하는 함수1 (행,열 우선순위 - 상,좌,하,우 순으로 탐색 방식)
def basecamp1(sx,sy):
    q = deque([(sx,sy)])
    
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            # 격자 범위 밖 or 방문한 베이스켐프/편의점 or 탐색한 경우
            if OOB(nx,ny) or vis[nx][ny]==1:
                continue
            # 베이스캠프  
            if block[nx][ny]==1:
                return nx,ny
            q.append((nx,ny))

# 가장 가까운 베이스캠프를 리턴하는 함수2 (행,열 우선순위 - 다 탐색해서 가장 빠른 좌표 리턴)
def basecamp2(sx,sy):
    check = [[0]*N for _ in range(N)]
    camps = []

    check[sx][sy] = 1
    q = deque([(sx,sy)])
    
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            # 격자 범위 밖 or 방문한 베이스켐프/편의점 or 탐색한 경우
            if OOB(nx,ny) or vis[nx][ny]==1 or check[nx][ny]==1:
                continue
            # 베이스캠프  
            if block[nx][ny]==1:
                camps.append((nx,ny))
            q.append((nx,ny))
            check[nx][ny] = 1   
    return sorted(camps, key=lambda x: (x[0],x[1]))[0]

def solve():
    for sx,sy in store:
        # store에서 가장 가까운 베이스캠프 찾기
        bx,by = basecamp1(sx-1,sy-1)
        # 찾은 베이스캠프 방문처리
        vis[bx][by]=1

        # 
       
       
       
       
        # print(bx,by)
        # for n in range(N):
        #     print(*vis[n])
        # print()


# 격자의 크기, 사람의 수
N,M = map(int,si().split())
# 격자의 정보 (0: 빈공간, 1: 베이스캠프)
block = [list(map(int,si().split())) for _ in range(N)]
# 편의점의 위치 (행,열)
store = [list(map(int,si().split())) for _ in range(M)]

# 베이스캠프/편의점 방문처리
vis = [[0]*N for _ in range(N)]

dx,dy = [-1,0,1,0], [0,-1,0,1]

solve()


# 모든 사람이 편의점에 도착하는 시간
rst = 0