'''
# [BOJ_1697 숨바꼭질 -Python3](https://www.acmicpc.net/problem/1697)

## 문제분석
```Python
1. 관찰
- 숨바꼭질을 하는데 수빈이는  걷거나, 순간이동을 할 수 있다.
- 걷기: x-1 or x+1
- 순간이동: 2*x
- 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구해라

2. 복잡도
- O(n)

3. 자료구조
- 거리 : int[n]

```

## 해결코드
```Python
'''
from collections import deque
import sys
si = sys.stdin.readline

n,k = map(int,si().split()) # 수빈이 위치, 수빈이 동생 위치
MAX = 10**5
dist = [0]*(MAX+1) # 거리

q = deque([n])
while q:
    now = q.popleft()
    if now == k:
        print(dist[now])
        break
    for nxt in (now-1, now+1, 2*now):
        if 0<= nxt <= MAX and not dist[nxt]:
            dist[nxt] = dist[now] + 1
            q.append(nxt) 