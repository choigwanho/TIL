'''
# [BOJ_13549 숨바꼭질 3 -Python3](https://www.acmicpc.net/problem/13549)

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
from collections import deque
si = sys.stdin.readline

n, k = map(int,si().split())

time = [-1 for _ in range(100001)]
time[n]=0

q = deque()
q.append(n)

while q:
    now = q.popleft()

    if now == k:
        print(time[now])
        break
    if 0<= 2*now < 100001 and time[2*now]==-1:
        time[2*now] = time[now]
        q.appendleft(2*now) # 2*now가 우선 순위를 가지도록 함
    if 0<= now+1 < 100001 and time[now+1]==-1:
        time[now+1] = time[now]+1 
        q.append(now+1)
    if 0<= now-1 < 100001 and time[now-1]==-1:
        time[now-1] = time[now]+1
        q.append(now-1)
    