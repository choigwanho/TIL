'''
# [BOJ_1463 1로 만들기 -Python3](https://www.acmicpc.net/problem/1463)

## 문제분석
```Python
1. 관찰
- 입력: 1000000 => 백만
- N%3 == 0 => nxt = N / 3
- N%2 == 0 => nxt = N / 2
- nxt = N - 1
- 출력: N을 1로 만드는 연산의 최소 횟수 

- 3 으로 나누기, 2로 나누기, 1빼기 순으로 진행할 수로 연산을 줄일 수 있다.

구하려는 값은 N을 1로 만드는 연산의 최소 횟수이다.
N이 1이 될때연산의 횟수는 이전의 연산에 영향을 받는다.
=> dp   1~N까지 기억하여 연산, cnt는 1,2,3이 되는데 필요한 연산 횟수를 초기화 하고 N이 될때 필요한 연산을 1에서 부터 N이 될때 까지 보텀엄 방식으로 연산한다.
dp  : 0 1 2 3 4 5 6 7 ...
cnt : 0 0 1 1 ... 점화식

보텀업 방식으로 연산
 
2. 복잡도
- O(N) = 10**6 >> 10만 가능

3. 자료구조
- dp : int[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

N = int(si())
dp = [0 for _ in range(N+1)]  

for n in range(2,N+1): # 2부터 N이 될때 까지 필요한 연산횟수 리턴
    # 1을 더하는 방식 2,3을 곱하는 방식 연산 횟수 비교하여 초기화
    if n%3==0 and n%2==0: 
        dp[n] = min(dp[n-1], dp[n//2], dp[n//3])+1
    elif n%3==0 and n%2!=0:
        dp[n] = min(dp[n-1], dp[n//3])+1
    elif n%3!=0 and n%2==0:
        dp[n] = min(dp[n-1], dp[n//2])+1
    else:
        dp[n] = dp[n-1] + 1 # dp[2], dp[3] 각각 연산횟수 1,1로 초기화됨
print(dp[N]) 