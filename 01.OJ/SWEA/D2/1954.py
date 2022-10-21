# 달팽이 숫자
from collections import deque
def bfs(arr,x,y):
    dir = [(0,1),(1,0),(0,-1),(-1,0)] # 동,남,서,북    
    q = deque([(x,y,0)])
    arr[x][y] = 1 
    while q:
        nx,ny,dir_idx= q.popleft()
        dx,dy = nx+dir[dir_idx][0],ny+dir[dir_idx][1]
        if arr[nx][ny] == N*N:
            return
        if 0<=dx<N and 0<=dy<N:
            if not arr[dx][dy]:
                arr[dx][dy] = arr[nx][ny]+1
                q.append((dx,dy,dir_idx))
            else:
                dir_idx=(dir_idx+1)%4
                q.append((nx,ny,dir_idx))
        else:
            dir_idx=(dir_idx+1)%4
            q.append((nx,ny,dir_idx))      
    
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    bfs(arr,0,0)
    print(f'#{t}')
    for row in arr:
        print(*row)

