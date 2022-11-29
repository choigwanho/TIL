'''
# [BOJ_14501 퇴사 -Python3](https://www.acmicpc.net/problem/14501)

## 문제분석
```Python
1. 관찰
- 소화할 수 있는 모든 조합을 구한다.
- 가능한 일정중에 이득의 합이 제일 큰 경우를 출력한다.

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
T = []
P = []
dp = []

for _ in range(N):
    t,p = map(int,si().split())
    T.append(t)
    P.append(p)
    dp.append(p)
dp.append(0)

for i in range(N-1,-1,-1):
    if i+T[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+T[i]] + P[i],dp[i+1])
print(dp[0])