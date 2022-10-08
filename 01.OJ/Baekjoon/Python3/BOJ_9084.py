'''
# [BOJ_9084 동전 -Python3](https://www.acmicpc.net/problem/9084)

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

for _ in range(int(si())):

    N = int(si())
    coins = list(map(int, si().split()))
    M = int(si())

    answer = 0

    for coin in sorted(coins, reverse=True):
        answer += M//coin
        M = M%coin

    print(answer)

    