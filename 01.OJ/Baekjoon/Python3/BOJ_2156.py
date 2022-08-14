'''
# [BOJ_2156 포도주 시식 -Python3](https://www.acmicpc.net/problem/2156)

## 문제분석
```Python
1. 관찰
- 포도주 잔이 일렬로 놓여 있다.
- 포도주는 마시고 원위치
- 연속으로 놓여 있는 3잔을 모두 마실 수 없다.

- 가장 많은 포도주를 마시는 방법을 구한다.

bottom up 방식으로 연산
- 초기화 dp[0 for _ in range(n+1)]
- 두 잔을 연속으로 마시는 경우 or 한 잔만 마시는 경우

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
wine = [0]
for i in range(N):
    wine.append(int(si()))

dp = [0]
dp.append(wine[1])
if N>1: 
    dp.append(wine[1]+wine[2]) 
for n in range(3,N+1): 
    dp.append(max(dp[n-1], dp[n-2]+wine[n], dp[n-3]+wine[n-1]+wine[n])) 
print(dp[N])
     
    
