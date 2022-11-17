'''
# [BOJ_13706 제곱근 -Python3](https://www.acmicpc.net/problem/13706)

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

N = int(si()) # 말도 안되게 큰 수

l, r = 0, N
while l<=r:
    mid = (l+r)//2
    want = mid**2
    if want==N:
        break
    elif want<N:
        l=mid+1
    elif want>N:
        r=mid-1
        
print(mid)