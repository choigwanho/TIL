'''
# [BOJ_2798 블랙잭 -Python3](https://www.acmicpc.net/problem/2798)

## 문제분석
```Python
1. 관찰
- N장의 카드 중에서 3장의 카드를 골라 M과 최대한 가까운 수를 만든다.
- 주어진 카드에서 3장을 뽑을 수 있는 모든 조합을 탐색한다.

2. 복잡도
- O(nC3) = 100! / (3!*97!) = (100*99*98)/(3*2*1) >> 가능

3. 자료구조
- 카드 = int[]

```

## 해결코드
```Python
'''
# from itertools import combinations
# import sys
# si = sys.stdin.readline

# N, M = map(int, si().split())
# cards = list(map(int, si().split()))


# picked = []

# ans = 0

# for picked in combinations(cards, 3):
#     sum_pick = sum(picked)
#     if sum_pick <= M:
#         ans = max(ans, sum_pick)

# print(ans)



import sys
si = sys.stdin.readline

N, M = map(int, si().split())
cards = list(map(int, si().split()))
ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_c = cards[i]+cards[j]+cards[k]
            if sum_c <=M:
                ans = max(ans,sum_c)

print(ans)
                


