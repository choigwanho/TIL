'''
# [BOJ_12865 평범한 배낭 -Python3](https://www.acmicpc.net/problem/12865)

## 문제분석
```Python
1. 관찰
- N개의 물건이 있다.
- 각 물건은 무게 W와 가치 V를 가진다.
- 최대 K만큼의 무게만을 배낭에 넣을 수 있다.
- 이때, 배낭에 넣을 수 있는 물건들의 가치의 최대값을 알아내야 한다.

2. 복잡도
- 

3. 자료구조
-

```

## 해결코드
```Python
'''
def knapsack(limit, wv_arr, quantity):
    dp = [[0 for _ in range(limit+1)] for _ in range(quantity+1)]
    for i in range(quantity + 1):
        for w in range(limit+1):
            if i == 0 or w==0:
                dp[i][w]==0
            elif wv_arr[i-1][0] <= w:
                dp[i][w] = max(wv_arr[i-1][1] + dp[i-1][w-wv_arr[i-1][0]], dp[i-1][w] )
            else:
                dp[i][w] =  dp[i-1][w]
    return dp[quantity][limit]

import sys

si = sys.stdin.readline

N, K = map(int, si().split())
stuff = list(list(map(int, si().split())) for _ in range(N))

print(knapsack(K, stuff, N))