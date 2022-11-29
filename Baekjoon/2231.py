'''
# [BOJ_2231 분해합 -Python3](https://www.acmicpc.net/problem/2231)

## 문제분석
```Python
1. 관찰
- 분해합: N을 이루는 각 자리수의 합
- m을 증가시켜가며 sum 을 N과 비교한다.
- N과 같을 때 출력하고
- N과 같은 경우가 없는 경우 for - else 구문으로 0을 출력한다.

2. 복잡도
- O(N) = 1,000,000 >> 가능

3. 자료구조
- 각자리수 분해 : int[] -> list(map(int, str(i)))
```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

N = int(si())
for i in range(1,N):
    s = i + sum(list(map(int,str(i))))
    if s == N:
        print(i)
        break 
else: # 생성자가 없는 경우 0 출력, for - else 구문
    print(0)
