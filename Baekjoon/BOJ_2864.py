'''
# [BOJ_2864 5와 6의 차이 -Python3](https://www.acmicpc.net/problem/2864)

## 문제분석
```Python
1. 관찰
- 5를 5나 6으로 보고, 6을 5나 6으로 본다.
- 최소값: 6을 5로 바꾼경우
- 최대값: 6을 5로 바꾼경우

2. 복잡도
- O(len(A)+len(B)) = 7+7 >> 매우가능

3. 자료구조
- 5,6 의 자리수 check: int[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

A,B = map(list,si().strip().split())
check_a = [0 for _ in range(len(A))]
check_b = [0 for _ in range(len(B))]

for i,v in enumerate(A):
    if v=='5' or v=='6':
        A[i]=0
        check_a[i]=1

for i,v in enumerate(B):
    if v=='5' or v=='6':
        B[i]=0
        check_b[i]=1

min_a = int("".join(map(str,A)))+5*int("".join(map(str,check_a)))
max_a = int("".join(map(str,A)))+6*int("".join(map(str,check_a)))

min_b = int("".join(map(str,B)))+5*int("".join(map(str,check_b)))
max_b = int("".join(map(str,B)))+6*int("".join(map(str,check_b)))

print(min_a+min_b, max_a+max_b)

