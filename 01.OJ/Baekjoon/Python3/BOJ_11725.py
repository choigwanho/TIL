'''
# [BOJ_11725 트리의 부모 찾기 -Python3](https://www.acmicpc.net/problem/11725)

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
# dfs
import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

n = int(si())
tree = list([] for _ in range(n+1))
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int,si().split())
    tree[u].append(v)
    tree[v].append(u)

# 1부터 부모노드를 지정
def dfs(start, graph, parent):
    for i in tree[start]:
        if parents[i]==0:
            parent[i] = start
            dfs(i, graph, parent)

dfs(1,tree, parents)

for i in range(2,n+1):
    print(parents[i])



    