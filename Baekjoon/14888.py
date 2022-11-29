'''
# [BOJ_14888 연산자 끼워넣기 -Python3](https://www.acmicpc.net/problem/14888)

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
from collections import deque
import sys
si = sys.stdin.readline

def sol():
    if used.count(1) == n-1:
        rst = a_list[0]
        for i in range(1,n):
            cal = chosen[i-1]
            if cal == '+':
                rst += a_list[i]
            if cal == '-':
                rst -= a_list[i] 
            if cal == '*':
                rst *= a_list[i]
            if cal == '/':
                if rst<0 and a_list[i]>0:
                    rst = -(-rst//a_list[i])
                else:
                    rst = rst//a_list[i]
        rst_list.append(rst)
        return
    for i in range(n-1):
        if not used[i]:
            used[i] = 1
            chosen.append(cals[i])
            sol()
            chosen.pop()
            used[i] = 0

n = int(si()) # 줄의 개수 2~11
a_list = list(map(int,si().split())) # len = n, a: 1~100
a,s,m,d  = map(int,si().split()) # sum(nums) = n-1, 4개의 정수

cals = list('+'*a+'-'*s+'*'*m+'/'*d)
used = list(0 for _ in range(n-1))
chosen=[]
rst_list = list()

sol()
print(max(rst_list),min(rst_list),sep='\n')

