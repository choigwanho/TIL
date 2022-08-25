'''
# [토딩테스트 고득점 Kit 깊이/너비 우선탐색(DFS/BFS) 타겟넘버 -Python3](https://school.programmers.co.kr/learn/courses/30/lessons/43165)

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
'''
def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0],[-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx+=1
        if idx<n:
            queue.append([temp+numbers[idx],idx])
            queue.append([temp-numbers[idx],idx])
        else:
            if temp == target:
                answer += 1
    return answer
'''
'''
from collections import deqeue
def solution(numbers, target):
    answer = 0
    q = deqeue()
    q.append([numbers[0],0])
    q.append([-1*numbers[0],0])
    n = len(numbers)
    while q:
        temp, idx = q.popleft()
        idx+=1
        if idx<n:
            q.append([temp+numbers[idx],idx])
            q.append([temp-numbers[idx],idx])
        else:
            if temp == target:
                answer += 1
    return answer
'''

def solution(numbers, target):
    result = 0
    def dfs(cnum, index):
        nonlocal result
        print(f'index => {index}, len numbers => {len(numbers)}')
        if index == len(numbers):
            if cnum == target:
                result += 1
            return
        print(f'index => {index}, cnum + numbers[index]] => {cnum + numbers[index]}')
        dfs(cnum + numbers[index], index+1)
        dfs(cnum - numbers[index], index+1)

    dfs(0, 0)
    return result

solution([1, 1, 1, 1, 1],3)