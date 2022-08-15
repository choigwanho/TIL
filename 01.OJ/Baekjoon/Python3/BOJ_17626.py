'''
# [BOJ_17626 Four Squares -Python3](https://www.acmicpc.net/problem/17626)

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

    if dp[n+1] - n*n >=0:
        dp[n] = dp[n+1] - n*n
        print(dp[n])
'''
import sys
si = sys.stdin.readline

N = int(si())
dp = [0]*(N+1)
dp[1] = 1

for i in range(2, N+1):
    m = 4
    for j in range(1, int(i**(1/2))+1):
        m = min(m,dp[i-(j**2)])
    dp[i] = m + 1
print(dp[N])