# [BOJ_7562 나이트의 이동 - Python3](https://www.acmicpc.net/problem/7562)
'''
### 문제 접근
```Python3
1. 아이디어
- 결과가 최소거리를 보장하는 BFS로 푼다.
2. 복잡도
- O(V+E) : 300*300 + 8*300*300 >> 가능
3. 자료구조
- 체스판: int[][]
```
'''
### 해결 코드
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    I = int(input())
    start_x,start_y=map(int,input().split())
    target_x,target_y=map(int,input().split())
    chess = [[0 for _ in range(I)] for _ in range(I)]

    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [1,-1,2,-2,2,-2,1,-1]

    q = deque()
    q.append([start_x, start_y])
    ans = 0

    while q:
        x, y = q.popleft()
        if x == target_x and y == target_y:
            print(0)
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < I and 0<= ny < I and not chess[ny][nx]:
                q.append([nx,ny])
                chess[ny][nx] = chess [y][x]+1
            if nx == target_x and ny == target_y:
                ans = chess[ny][nx]

        if ans:
            print(ans)
            break