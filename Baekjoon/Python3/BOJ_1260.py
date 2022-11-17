# [BOJ_1260 DFS와 BFS - Python3](https://www.acmicpc.net/problem/1260)
'''
### 문제 분석
1. 아이디어
- bfs
- dfs
2. 복잡도
- O(V+E): 2000 >> 가능
- V : 1000
- E : 1000
3. 자료구조
- 그래프: int[][]
- 방문기록: bool[][]
```
## 해결 코드
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int, input().strip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for e in graph:
    e.sort()

visited_b =[False]*(n+1)
visited_d =[False]*(n+1)

def dfs(start):
    visited_d[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited_d[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited_b[start] = True
    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if not visited_b[i]:
                visited_b[i] = True
                q.append(i)

dfs(v)
print()
bfs(v)
