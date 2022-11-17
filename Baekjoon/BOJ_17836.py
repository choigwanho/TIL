'''
# [BOJ_17836 공주님을 구해라! -Python3](https://www.acmicpc.net/problem/17836)

## 문제분석
```Python
1. 관찰
- bfs로 공주에게 도달하는 시간을 구한다.
- 그람까지 bfs + 벽을 무시하고 공주에게 도달하는 최단거리를 구한다.
- !! 그람을 발견하면 공주와의 거리는 사칙연산으로 구할 수 있다. 시간복잡도를 줄이자.
- 둘 중의 작은 값이 T보다 작으면 최소값 출력
- 구출하지 못하는 경우 fail

2. 복잡도
- O(N*M) = 100*100 >> 1만 가능

3. 자료구조
- 성 int[][]
- 방문여부 int[][]

```

## 해결코드
```Python
'''

import sys
from collections import deque
si = sys.stdin.readline

N, M, T = map(int, si().split())
castle = [list(map(int, si().split())) for _ in range(N)]
check = [list(0 for _ in range(M)) for _ in range(N)]

q = deque()
q.append((0,0,0))
result = float('inf')
while q:
    x, y, t = q.popleft()
    if x == M-1 and y == N-1: # 공주위치 도착
        result = min(result, t)
        break
    if t+1>T: #시간초과
        break 
    for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + i, y + j
        if 0 <= nx < M and 0 <= ny < N and not check[ny][nx]:
            if castle[ny][nx] ==1:
                continue
            elif castle[ny][nx]==0:
                check[ny][nx]=1
                q.append((nx,ny,t+1))
            else:    
                check[ny][nx]=1
                gramT = t + 1 + abs((N-1)-ny) + abs((M-1)-nx)
                if gramT<=T: 
                    result=gramT


if result>T: 
    print("Fail")
else:
    print(result)