'''
# [BOJ_1026 보물 -Python3](https://www.acmicpc.net/problem/1026)

## 문제분석
```Python
1. 관찰
- A의 최소와 B의 최대를 곱해준다.

2. 복잡도
- O(N*N*N) = 50*50*50 >> 가능

3. 자료구조
- A, B : int[]

```

## 해결코드
```Python
'''

import sys
si = sys.stdin.readline

N = int(si())
A = list(map(int,si().split()))
B = list(map(int,si().split()))

A.sort() # 오름차순 정렬
ans = 0 
for i in range(N):
    x, y = A[i], B.pop(B.index(max(B))) # 최소값, 최대값
    ans += x*y

print(ans)
