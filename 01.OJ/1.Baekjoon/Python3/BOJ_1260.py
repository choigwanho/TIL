# [BOJ_1260 DFS와 BFS - Python3](https://www.acmicpc.net/problem/1260)
'''
## 문제 분석
1. 아이디어
- m(간선의 개수)만큼 탐색
-
2. 복잡도
-
3. 자료구조
-

```
visited = [False]*(N+1)

def dfs(n):
    visited[n] =True
    print(n, end=" ")
    for i in graph[n]:
        dfs(i)

def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        v=queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            queue.append(i)
            visited[i] = True
```
## 해결 코드
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int, input())
graph = [list(map(int, input().split())) for _ in range(m)]

q = deque() # bfs


def dfs():


def bfs(n):



