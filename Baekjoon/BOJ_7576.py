'''
# [BOJ_7576 토마토 -Python3](https://www.acmicpc.net/problem/7576)

## 문제분석
```Python
1. 관찰
- exit(0): 성공적인 종료
- exit(1): 비정상 종료

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
from collections import deque
import sys
si = sys.stdin.readline

m,n = map(int,si().split()) # 상자의 크기
box = list(list(map(int,si().split())) for _ in range(n))
q = deque([])
dx,dy = [-1,1,0,0], [0,0,-1,1]
ans=0

for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            q.append((i,j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            q.append((nx, ny))

for row in box:
    for apple in row:
        if apple == 0: # 익지 않은 토마토가 있으면 -1 출력 후 종료
            print(-1)
            exit(0)
        else:
            if ans<apple:
                ans=apple # 각 행을 돌며 최대 소요일 갱신
print(ans - 1)