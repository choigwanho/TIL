# [BOJ_10870 피보나치 수 5 - Python3](https://www.acmicpc.net/problem/10870)
'''
### 문제 접근
1. 아이디어
- 재귀함수
- for loop
2. 복잡도
-
3. 자료구조
-
'''
### 해결 코드
import sys
input = sys.stdin.readline

#### 1) 재귀 함수
def f(n):
    if n <=1:
        return n
    return f(n-1) + f(n-2)

n = int(input())
print(f(n))

#### 2) loop
f = [0, 1]
for i in range(2, n+1):
    num = f[i-1] + f[i-2]
    f.append(num)
print(f[n])



