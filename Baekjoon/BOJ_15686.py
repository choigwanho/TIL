# [BOJ_15686 치킨 배달 - Python3](https://www.acmicpc.net/problem/15686)
"""
## 문제 분석
```Python
1. 관찰
- 전체 치킨 집에서 중복없이 M 개의 치킨집을 선택하여 탐색
- combinations를 통해 m개 선택한 경우에 대하여 최소값의 합을 구한다.

2. 복잡도
- O(N*N) = 50*50 상수배 >> 가능

3. 자료구조
-
```
'''
"""
## 해결 코드

import sys
si = sys.stdin.readline
from itertools import combinations

N, M = map(int, si().split())

h = [] # 집의 위치
c = [] # 치킨집의 위치

for i in range(N):
    tmp = list(map(int, si().split()))
    for j in range(N):
        if tmp[j] == 1:
            h.append([i,j])
        if tmp[j] == 2:
            c.append([i,j])


ans = float("inf")

for chicken in combinations(c, M):
    sum = 0
    for hou in h:
        sum += min([abs(hou[0]-chi[0])+abs(hou[1]-chi[1]) for chi in chicken])
    if ans>sum:
        ans = min(ans, sum)
print(ans)