'''
# [BOJ_1535 안녕 -Python3](https://www.acmicpc.net/problem/1535)

## 문제분석
```Python
1. 관찰
- N명의 사람에게 감사해야한다.
- L[i]만큼 체력을 잃고 J[i]만큼 기쁨을 얻는다.
- 주어진 체력내에서 최대한의 기쁨을 얻어야한다.

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
L = [0]+list(map(int, si().split()))
J = [0]+list(map(int, si().split()))

dp = [[0]*101 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,101):
        if L[i]<=j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][99])    
