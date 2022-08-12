'''
# 프로그래머스 코딩테스트 실전 대비 모의고사 2차 - 2번  -Python3

## 문제분석
```Python
1. 관찰
- 토핑 일렬
- 롤케이크 반반
- 토핑의 종류 => 개수에 상관없이 동일한 가지수의 토핑
- for 문으로 나눌수 있는 구간 완전 탐색

2. 복잡도
- 시간초과

3. 자료구조
-

```

## 마지막 코드
```Python
'''
def solution(topping):
    tp = set(topping) 
    answer = 0
    
    for i in range(1,len(topping)):
        yb = len(set(topping[:i]))
        ob = len(set(topping[i:]))
        if yb==ob:
            answer += 1
        if yb>ob:
            break
    return answer

solution([1,2,3,1,4])


# 시간초과 코드 1
'''
def solution(topping):
    answer = 0
    
    for i in range(1,len(topping)):
        yb = len(set(topping[:i]))
        ob = len(set(topping[i:]))
        if yb==ob:
            answer += 1
    return answer

solution([1,2,3,1,4])
'''

# 시간초과 코드 2
'''
from collections import Counter
def solution(topping): # 100만 
    answer = 0
    for i in range(1,len(topping)):
        yb = len(Counter(topping[:i])) # Counter O(n) -> 100만
        ob = len(Counter(topping[i:]))
        if yb==ob:
            answer += 1
    return answer
'''