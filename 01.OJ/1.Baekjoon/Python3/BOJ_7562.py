# [BOJ_7562 나이트의 이동 - Python3](https://www.acmicpc.net/problem/7562)
'''
### 문제 접근
```Python3
1. 아이디어
- 최소거리를 보장하는 BFS로 푼다.

2. 복잡도
- O(V+E) : 300*300 + 8*300*300

3. 자료구조
-

```
'''
### 해결 코드
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    I = int(input())
    start_x,start_y=map(int,input().strip().split())
    target_x,target_y=map(int,input().strip().split())

    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [1,-1,2,-2,2,-2,1,-1]

    def bfs():
        q = deque()
        q.append([start_x,start_y])
        result=0
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0<= nx < I and 0<= ny < I:
                    q.append([nx,ny])
                    result += 1
                    if nx == target_x and ny == target_y:
                        print(result)
                        break
    bfs()