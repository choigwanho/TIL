from collections import deque

def solution(board, aloc, bloc):
    answer = -1 # 양 를레이어가 캐릭터를 움직이는 횟수

    r = len(answer)
    c = len(answer[0])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque([]) 

    # 항상 이기는 플레이어 판단은 어떻게 하는가
        # 확실하게 지는 경우
            # 일단 만나서 -> 움직이려는 친구가 상하좌우의 발판이 없는 경우 or 한 친구가 움직여서 발판이 사라지는 경우
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=r or ny<0 or ny>=c:
                continue
            if board[nx][ny]==1:
                q.append()

        
    return answer

tc = [[[[1, 1, 1], [1, 1, 1], [1, 1, 1]],	[1, 0],	[1, 2], 5],    
      [[[1, 1, 1], [1, 0, 1], [1, 1, 1]],	[1, 0],	[1, 2], 4],    
      [[[1, 1, 1, 1, 1]],	[0, 0],	[0, 4], 4],                    
      [[[1]],	[0, 0],	[0, 0], 0]]                                
for board, aloc, bloc, result in tc:
    outcome = solution(board, aloc, bloc)
    print(outcome, result==outcome)