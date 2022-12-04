'''
* 2178 미로 탐색
* https://www.acmicpc.net/problem/2178
1. 아이디어
- 최단거리 탐색 문제
- BFS는 현재 노드에서 가까운 곳부터 찾기 때문에 경로 탐색 시 첫번째로 찾아지는 해답이 최단거리임을 보장
- 상하좌우 모두 탐색
- 상하좌우 좌표가 미로의 범위 밖 or 0이면 탈락
2. 복잡도
- 상하좌우 BFS O(n)
3. 자료구조
- 리스트, 큐
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())    # n줄, 길이 m짜리 입력
maze = list(list(map(int,' '.join(input()).split())) for _ in range(n))    # ' '.join(input()) 입력된 문자열을 ' '간격을 하나의 문자열로 반환

# 이동
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque([(0,0)])

while q:
    x,y=q.popleft()
    for i in range(4):    # 상하좌우 방문
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:    # 미로의 범위내에 있고
            if maze[nx][ny]==1:    # 다음이 1이라면
                #방문처리
                maze[nx][ny]=maze[x][y]+1    # 탐색하면서 미로에 이동거리 업데이트
                q.append((nx,ny))    # 방문 노드
print(maze[n-1][m-1])   # 도착 좌표 이동거리 출력