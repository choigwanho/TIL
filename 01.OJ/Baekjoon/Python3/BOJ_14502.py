'''
* 14502 연구소
* https://www.acmicpc.net/problem/14502
1. 아이디어
- 벽은 3개만 세울수 있다.
- 2의 상하좌우==0 인 경우를 모두 카운팅해본다. 3개 이상이다 아니다로 일단 구분
-
2. 복잡도
-
3. 자료구조
-
-
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
q = deque()

def bfs():
    global result

for i in range(n):
    for j in range(m):
        continue