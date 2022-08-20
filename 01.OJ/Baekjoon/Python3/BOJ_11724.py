'''
# [BOJ_11724 연결 요소의 개수 -Python3](https://www.acmicpc.net/problem/11724)

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
import sys
si = sys.stdin.readline
sys.setrecursionlimit(10000) # python 재귀제한 문제에서 주어진 10000으로 설정

def dfs(v): # 
    check[v]=1
    for i in graph[v]:
        if not check[i]:
            dfs(i)

n,m = map(int,si().split())
graph=list([] for _ in range(n+1))
check = [0]*(n+1)
ans=0

for i in range(m):
    u,v = map(int,si().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, n+1):
    if not check[i]:
        dfs(i)
        ans+=1
print(ans)
