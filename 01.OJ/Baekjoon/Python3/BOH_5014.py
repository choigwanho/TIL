'''
# [BOJ_5014 스타트링크 -Python3](https://www.acmicpc.net/problem/5014)

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
def bfs(start):
    floor = [0 for _ in range(F+1)]
    visited = [0 for _ in range(F+1)]

    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        
        if now == G:
            return floor[G]
            
        for nxt in [now+U,now-D]:
            if 0< nxt <=F and not visited[nxt]:
                visited[nxt] = 1
                floor[nxt]=floor[now]+1
                q.append(nxt)
                
    if floor[G] == 0:
        return 'use the stairs'

import sys
from collections import deque
si = sys.stdin.readline

F,S,G,U,D = map(int,si().split()) 

print(bfs(S))