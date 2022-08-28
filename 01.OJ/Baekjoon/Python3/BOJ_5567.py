'''
# [BOJ_5567 결혼식 -Python3](https://www.acmicpc.net/problem/5567)

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

n = int(si())
m = int(si())

rel = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,si().split())
    rel[a].append(b)
    rel[b].append(a)


wed = []
q = deque([1])
while q:
    now = q.popleft()
    for nxt in rel[now]:
        if nxt not in wed:
            if now == 1: # 상근이 친구들 추가
                wed.append(nxt)
                q.append(nxt)
            if 1 in rel[now]: # 상근이 친구의 친구 추가
                if nxt == 1:
                    continue
                wed.append(nxt)
                q.append(nxt)
print(len(wed))