'''
# 프로그래머스 코딩테스트 실전 대비 모의고사 3차 - 1번  -Python3

## 문제분석
```Python
1. 관찰


2. 복잡도

3. 자료구조


```

## 해결코드
```Python
'''
answer = 0
def solution(a, b, n):
    global answer
    answer += (n//a)*b
    n = (n%a) + (n//a)*b # 가지고 있는 콜라 수 = 나머지 + 빈병으로 받은 새병
    if n < a: # 더이상 병을 받을 수 없음
        return print(answer)
    solution(a, b, n)  

import sys
si = sys.stdin.readline

A,B,N = map(int,si().split())
solution(A,B,N)