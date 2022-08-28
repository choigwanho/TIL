'''
# [BOJ_11060 점프 점프 -Python3](https://www.acmicpc.net/problem/11060)

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

N = int(si())
A = list(map(int,si().split()))
dp = list(0 for _ in range(N+1))

for i in range(N):
    

while q:
    now, ndx = q.popleft()
    for i in range(now+1):
        idx = ndx + i
        if 0<= idx < N:
            if not visited[idx]:
                visited[idx] = 1
                q.append((A[idx],idx))
print(visited)
        
