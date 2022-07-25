# [BOJ_15649 N과 M (1) - Python3](https://www.acmicpc.net/problem/15649)
'''
### 문제 접근
```Python
1. 아이디어
- 백트래킹 재귀함수 안에서 for loop를 돌면서 숫자 선택 & 방문여부 확인
- 재귀함수에서 M개를 선택할 경우 print

2. 복잡도
- N! > 가능(8까지 가능)

3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]

```
'''
### 해결 코드

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
result = []
check = [False]*(N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if check[i] == False:
            check[i] = True # 방문
            result.append(i)
            recur(num+1)
            check[i] = False
            result.pop()

recur(0)