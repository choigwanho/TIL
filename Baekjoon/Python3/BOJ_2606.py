'''
# [BOJ_2606 바이러스 -Python3](https://www.acmicpc.net/problem/2606)

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
from collections import deque
import sys
si = sys.stdin.readline

def bfs(virus):
    global ans
    visited[virus]=1
    q = deque([1])
    while q:
        for nxt in graph[q.popleft()]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append(nxt)
                ans+=1

n = int(si())
v = int(si())
graph = list([] for _ in range(n+1))

for _ in range(v):
    n1,n2=map(int,si().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


ans =0
visited = [0]*(n+1)
bfs(1)

print(ans)


