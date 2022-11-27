import sys
si = sys.stdin.readline

# 변수 선언 및 입력:

# 격자의 크기(n), 플레이어의 수(m), 라운드의 수(k)
n,m,k = tuple(map(int,si().split()))

# 격자에 있는 총의 정보(n*n)
gun = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    nums = list(map(int,si().split()))
    for j in range(n):
        # 0!인 칸, 총 놓기
        if nums[j]!=0:
            gun[i][j].append(nums[j])

# 플레이어들의 정보(m*6)
players = []
for i in range(m):
    # 플레이어의 위치(x,y), 방향(d), 초기 능력치(s)
    x,y,d,s = tuple(map(int,si().split()))
    # 플레이어 번호(i), 들고있는 총의 공격력(0) 으로 관리
    players.append((i,x-1,y-1,d,s,0)) 

# 선수 EMPTY 정의
EMPTY = (-1, -1, -1, -1, -1, -1)

# 방향은 0부터 3까지 순서대로 상,좌,하,우
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 각 플레이어들이 획득한 포인트를 
points = [0]*m

def OOB(x,y):
    return x<0 or x>=n or y<0 or y>=n

def get_next(x,y,d):
    nx,ny = x + dx[d], y + dy[d] 
    if OOB(nx,ny):
        d = (d+2)%4
        nx,ny = x + dx[d], y + dy[d]
    return (nx,ny,d)

def find_player(pos):
    for i in range(m):
        _,x,y,_,_,_ = players[i]
        if pos == (x,y):
            return players[i]
    return EMPTY

def update(p):
    for i in range(m):
        if i == p[0]:
            players[i]=p
            break

def move_and_change_gun(p,pos):
    n,x,y,d,s,a = p
    nx,ny = pos

    gun[nx][ny].append(a)
    gun[nx][ny].sort()
    a = gun[nx][ny].pop()

    p = (n,nx,ny,d,s,a)
    update(p)
    
def move_loser(p):
    n,x,y,d,s,a = p

    gun[x][y].append(a)

    for i in range(4):
        ndir = (d+i)%4
        nx, ny = x + dx[ndir], y + dy[ndir]
        if not OOB(nx,ny) and find_player((nx,ny))==EMPTY:
            p = (n,x,y,ndir,s,0)
            move_and_change_gun(p,(nx,ny))
            break

def duel(p1,p2,pos):
    n1,_,_,d1,s1,a1 = p1
    n2,_,_,d2,s2,a2 = p2

    if (s1+a1,s1)>(s2+a2,s2):
        points[n1] += (s1+a1)-(s2+a2)
        move_loser(p2)
        move_and_change_gun(p1,pos)
    else:
        points[n2] += (s2+a2)-(s1+a1)
        move_loser(p1)
        move_and_change_gun(p2,pos)

def simulate():
    for i in range(m):
        n,x,y,d,s,a = players[i]

        # 1-1. 현재 플레이어가 움직일 다음 위치와 방향 구하여 한칸 이동 (위치 업데이트)
        nx,ny,ndir = get_next(x,y,d)
        curr_player = (n,nx,ny,ndir,s,a)
        update(curr_player)

        # 해당 위치에 있는 플레이어 정보 구하기 (한 사람만 겹치게 됨)
        opponent_player = find_player((nx,ny))

        # 2-1. 해당 위치에 플레이어가 없으면 총 획득 (총 업데이트)
        if opponent_player == EMPTY:
            move_and_change_gun(curr_player,(nx,ny))
        # 2-2. 해당 위치에 플레이어가 있으면 싸움, 진 플레이어는 이동, 이긴 플레이어는 포인트 획득
        else:
            duel(curr_player, opponent_player,(nx,ny))

for _ in range(k):
    simulate()

print(*points)