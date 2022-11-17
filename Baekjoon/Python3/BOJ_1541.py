'''
# [BOJ_1541 잃어버린 괄호 -Python3](https://www.acmicpc.net/problem/1541)

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

poly = list(si().strip().split('-'))
num = []

for p in poly:
    sum = sum(map(int, p.split('+')))
    num.append(sum)

print(num[0]-sum(num[1:]))
    



