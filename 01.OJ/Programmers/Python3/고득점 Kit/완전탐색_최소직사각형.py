'''
# [코딩테스트 고득점 Kit 완전탐색 최소직사각형 -Python3](https://school.programmers.co.kr/learn/courses/30/lessons/86491)

## 문제분석
```Python
1. 관찰
- 주어진 사이즈 배열안에 사이즈을 각각 오름차순으로 정렬하여, 가로, 세로의 최대값을 구하여 최소 지갑 크기를 찾는다. 

2. 복잡도
-  

3. 자료구조
- 사이즈 : int[]

```

## 해결코드
```Python
'''

def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort()
    w = max(sizes, key = lambda x: x[:][0])[0]
    h = max(sizes, key = lambda x: x[:][1])[1]
    answer=w*h
    
    return answer