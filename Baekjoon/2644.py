'''
# [BOJ_2644 촌수계산 -Python3](https://www.acmicpc.net/problem/2644)

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

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        s = q.popleft()
        for node in tree[s]:
            if not check[node]:
                check[node] = check[s]+1
                q.append(node)

n = int(si())
tree = list([] for _ in range(n+1))
a, b = map(int,si().split())
for _ in range(int(si())):
    x,y = map(int,si().split())
    tree[x].append(y)
    tree[y].append(x)
check = list(0 for _ in range(n+1))

bfs(a)

if not check[b]:
    print(-1)
else:
    print(check[b])
