'''
# [BOJ_1065 한수 -Python3](https://www.acmicpc.net/problem/1065)

## 문제분석
```Python
1. 관찰
- 한수: x의 각 자리가 등차수열을 이루는 수
- 범위가 1000 미만의 수에 한정되어있으므로 세자리 수 까지 고려한다.
- 2자리 수 까지는 모두 한수
- 3자리 수는 값의 차이를 직접 비교하여 맞는 경우만 카운트한다.

2. 복잡도
- O(N) = 999 >> 가능

3. 자료구조
- 한수: int

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

N = int(si())

num = 0
ans = 0
while num < N:
    num += 1
    if num < 100: # 2자리수 까지는 모두 한수
        ans+=1
    if 100 <= num: # 3자리 한수는 차이를 비교
        a,b,c = num//100, (num%100)//10, num%10

        if a-b == b-c:
            ans+=1

print(ans)