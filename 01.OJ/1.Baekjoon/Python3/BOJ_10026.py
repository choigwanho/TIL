'''
* 10026 적록색약
* https://www.acmicpc.net/problem/10026
1. 아이디어
- 인접한 픽셀의 색이 같은 경우 dfs
- 방문하지 않은 노드에 대하여 dfs 반복하여 모든 그룹 카운팅
- 적록색맹의 경우 R,G를 통일하여 같은 방식으로 그룹 탐색
2. 복잡도
- O(n*2)
3. 자료구조
- 재귀, 리스트
'''

import sys
sys.setrecursionlimit(10 ** 6) # 재귀 최대 깊이 설정( 파이썬의 재귀 최대 깊이의 기본 설정이 1,000회 이기 때문에 추가 필요)
input = sys.stdin.readline

n = int(input().rstrip())
pic = [list(input().rstrip()) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

dxdy = [[-1,0],[1,0],[0,-1],[0,1]]
rg_y_cnt, rg_n_cnt = 0, 0

# 색상이 같은 경우 dfs하여 그룹 방문처리
def dfs(x,y):
    # 현재 색상 좌표를 방문
    visited[x][y]= True # 방문처리
    current_color = pic[x][y]

    for dir in dxdy: # 상하좌우 방문
        nx,ny = x+dir[0],y+dir[1]
        if 0<= nx <n and 0<= ny <n:  # 범위 내에 있고
            if visited[nx][ny]==False: # 미방문인 경우
                if pic[nx][ny] == current_color: # 현재 좌표의 색상과 상하좌우 좌표 색상이 같으면 끝까지 탐색
                    dfs(nx,ny)

# 미방문인경우 dfs하여 그룹 탐색
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            dfs(i,j)
            rg_y_cnt+=1

# 적록색맹의 경우 R,G 구분 못 하므로 G로 통일
for i in range(n):
    for j in range(n):
        if pic[i][j]=='R':
            pic[i][j]='G'

# 방문처리 초기화
visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            dfs(i,j)
            rg_n_cnt+=1

print(rg_y_cnt,rg_n_cnt)
