from collections import deque
def solution(maps):
    answer = 0
    r,c = len(maps), len(maps[0])
    xy = [(-1,0),(1,0),(0,-1),(0,1)]
    
    q = deque()
    q.append([0,0])
    while q:
        ny,nx = q.popleft()
        for d in xy:
            dy,dx = ny + d[0], nx + d[1]
            if 0 <= dy < r and 0 <= dx < c:
                if maps[dy][dx]==1:
                    q.append([dy,dx])
                    maps[dy][dx]=maps[ny][nx]+1
                            
    if maps[r-1][c-1] > 1:
        answer = maps[r-1][c-1]
    else:
        answer = -1
        
    return answer  

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])