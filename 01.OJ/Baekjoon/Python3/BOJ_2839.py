'''
# [BOJ_2839 설탕 배달 -Python3](https://www.acmicpc.net/problem/2839)

## 문제분석
```Python
1. 관찰
- 정확히 N 킬로 배달
- 3, 5 킬로 봉지로 배달할 때 봉지의 최소 개수

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
ans=0

dp = [5001]*(N+6)
dp[3]=dp[5]=1
for i in range(6,N+1):
    dp[i] = min(dp[i-3],dp[i-5])+1
print(dp[N] if dp[N] < 5001 else -1)
