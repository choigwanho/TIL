'''
# [BOJ_2589 보물섬 -Python3](https://www.acmicpc.net/problem/2589)

## 문제분석
```Python
1. 관찰
-

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
def bfs(x,y):
    visited = [[0 for _ in range(C)] for _ in range(R)]
    q = deque([(x,y,0)])
    visited[x][y]=1
    max_cnt = 0 
    while q:
        nx,ny,cnt = q.popleft()
        max_cnt = max(max_cnt,cnt)
        for x_dir,y_dir in [(-1,0),(1,0),(0,-1),(0,1)]:
            dx,dy = nx+x_dir, ny+y_dir
            if dx<0 or dx>=R or dy<0 or dy>=C: 
                continue
            if not visited[dx][dy] and arr[dx][dy]=='L':
                visited[dx][dy] = 1
                q.append((dx,dy,cnt+1))
    return max_cnt

import sys
from collections import deque

si = sys.stdin.readline

R,C = map(int,si().split()) # 가로, 세로 크기
arr = [list(si().strip()) for _ in range(R)] 
ans = 0

for i in range(R):
    for j in range(C):
        if arr[i][j]=='L':
            ans = max(ans, bfs(i,j))

print(ans)