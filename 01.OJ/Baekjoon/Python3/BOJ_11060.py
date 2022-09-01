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
dp = [N+1]*N
dp[0]=0
for i in range(N):
    for j in range(1,A[i]+1):
        if i+j >= N:
            break       
        dp[i+j] = min(dp[i+j],dp[i]+1) 
print(dp[N-1] if dp[N-1]!=N+1 else -1)


'''
n = int(input())
lst = list(map(int, input().split()))

dp = [-1] * n

def bfs(start):
    q = []
    q.append(start)
    dp[start] = 0
    while q:
        now = q.pop(0)
        jump = lst[now]
        for i in range(jump, 0, -1):
            if now + i < n and dp[now + i] == -1:
                dp[now + i] = dp[now] + 1
                q.append(now + i)

bfs(0)
print(dp[-1])

'''