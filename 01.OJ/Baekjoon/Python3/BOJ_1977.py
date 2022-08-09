'''
# [BOJ_1977 완전제곱수 -Python3](https://www.acmicpc.net/problem/1977)

## 문제분석
```Python
1. 관찰
- M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합과 그 중 최소값을 찾는다.
- 완전제곱수를 찾는 것이므로 i의 제곱근 범위까지만 탐색한다.

2. 복잡도
- O((N-M+1)*(N**(1/2))) = 1000000*100 >> 100만 가능

3. 자료구조
- 완전제곱수 : int[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

M = int(si())
N = int(si())
nums = []

for i in range(M,N+1):
    for j in range(1,int(i**(1/2))+1):
        if i == j*j:
            nums.append(i)

if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)