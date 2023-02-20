from collections import deque
import sys
si = sys.stdin.readline

N, M = map(int,si().split()) # 보드의 세로, 가로
board = list(list(si().rstrip()) for _ in range(N)) # 보드, 빈칸 : ".", 이동할 수 없는 벽 : "#", 구멍의 위치 : "O", 빨간 구슬의 위치 : "R", 파란 구술의 위치 : "B"

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([])

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N): 
        for j in range(M):
            if board[i][j] == "R":
                rx, ry = i, j
            elif board[i][j] == "B":
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0 
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def sol():
    init()
    while q:
        rx, ry, bx, by , depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] != "O":
                if board[nrx][nry] == "O":  # 성공 조건
                    print(depth)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, depth + 1))
    print(-1)

sol() # 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력, 10번 이하로 움직여서 빼낼 수 없으면 -1 출력