'''
2022 카카오 신입 공채 1차 온라인 코딩테스트 문제 7번 - 사라지는 발판

# 문제읽기
- 양 플레이어가 캐릭터를 몇 번 움직이게 될지 예측하는 문제

- 발판이 있는 곳에만 캐릭터가 서있을 수 있으
- 캐릭터는 발판이 있는 곳으로만 이동할 수 있으
- 밟고 있던 발판은 그 위에 있던 캐릭터가 다른 곳으로 이동하여 다른 발판을 밟음과 동시에 사라집
- 양 플레이어는 번갈아가며 자기 차례에 자신의 캐릭터를 상하좌우로 인접한 4개의 칸 중에서 발판이 있는 칸으로 옮겨야 합
- 항상 플레이어 A가 먼저 시작

- 이길 수 있는 플레이어는 최대한 빨리 승리하도록 플레이
- 질 수밖에 없는 플레이어는 최대한 오래 버티도록 플레이
- 양 플레이어가 캐릭터를 움직이는 횟수를 최대화

# 아이디어 설계
- board의 크기가 최대 5*5 로 크기가 크지않고, 발판이 사라지는 조건이 있으므로 탐색의 경우의 수가 줄어들어 완전 탐색 가능
- 보드의 상태와 a, b의 위치를 매개변수로 하고
- 승자와 총 이동 횟수를 리턴하는 함수 완성

# 시간복잡도 검증
- 

# 자료구조 계획
- 

'''

dx, dy = [-1,1,0,0], [0,0,-1,1]
N,M = 0, 0

vis = [[0]*5 for _ in range(5)]
block = [[0]*5 for _ in range(5)]

def OOB(x,y):
    return x<0 or x>=N or y<0 or y>=M

def solve(curx,cury,opx,opy):
    global vis, block

    if vis[curx][cury]: return 0
    ret = 0

    for dir in range(4):
        nx = curx + dx[dir]
        ny = cury + dy[dir]
        if OOB(nx,ny) or vis[nx][ny] or block[nx][ny]==0: continue

        vis[curx][cury] = 1
        val = solve(opx,opy,nx,ny)+1
        vis[curx][cury] = 0

        if ret % 2 ==0 and val % 2 == 1: ret = val
        elif ret % 2 == 0 and val % 2 == 0: ret = max(ret, val)
        elif ret % 2 == 1 and val % 2 == 1: ret = min(ret, val)

    return ret

def solution(board, aloc, bloc):
    global N,M 
    N = len(board)
    M = len(board[0])
    for i in range(N):
        for j in range(M):
            block[i][j] = board[i][j]
    return solve(aloc[0],aloc[1],bloc[0],bloc[1])

tc = [[[[1, 1, 1], [1, 1, 1], [1, 1, 1]],	[1, 0],	[1, 2], 5],    
      [[[1, 1, 1], [1, 0, 1], [1, 1, 1]],	[1, 0],	[1, 2], 4],    
      [[[1, 1, 1, 1, 1]],	[0, 0],	[0, 4], 4],                    
      [[[1]],	[0, 0],	[0, 0], 0]]   

for board, aloc, bloc, result in tc:
    outcome = solution(board, aloc, bloc)
    print(outcome, result==outcome)