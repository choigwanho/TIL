'''
# [BOJ_5585 거스름돈 -Python3](https://www.acmicpc.net/problem/5585)

## 문제분석
```Python
1. 관찰
- 500, 100, 10, 5, 1 로 거스름돈을 받는다.
- 1000엔을 냈을 때 받는 잔돈의 개수를 구해야한다.
- 거스름돈 개수가 가장 적은 경우에 개수를 출력한다.

- 거스름돈이 가장 적은 경우는
- 큰돈부터 차례대로 값을 채워나가는 경우이다

2. 복잡도
- 사칙연산 

3. 자료구조
- 거스름 최소경우 : int[]

```

## 해결코드
```Python
'''

# sol 1
import sys
si = sys.stdin.readline

pay = int(si())
m = 1000-pay

payback = [m//500,m%500//100,m%500%100//50,m%500%100%50//10,m%500%100%50%10//5,m%500%100%50%10%5]
print(sum(payback))


# sol 2
import sys
si = sys.stdin.readline

n = int(si()) # 지불할 돈
l = [500,100,50,10,5,1]

m = 1000-n
cnt = 0
for cash in l:
    cnt += m//cash
    m = m%cash

print(cnt)