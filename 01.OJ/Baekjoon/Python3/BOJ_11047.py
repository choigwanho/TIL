'''
# [BOJ_11047 동전 0 -Python3](https://www.acmicpc.net/problem/11047)

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

n,k = map(int,si().split())
coins = list()
for _ in range(n):
    coins.append(int(si()))

ans = 0
for i in range(n-1,-1,-1):
    ans += k//coins[i]
    k = k%coins[i]

print(ans)

    
