'''
# [BOJ_11399 ATM -Python3](https://www.acmicpc.net/problem/11399)

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

n = int(si())
atm = list(map(int,si().split()))
atm.sort()
ans = 0
for i in range(1,n+1):
    ans+=sum(atm[:i])
print(ans)