'''
# [BOJ_10974 모든 순열 -Python3](https://www.acmicpc.net/problem/10974)

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

N = int(si())
tmp =[]

def permutation():
    if len(tmp)==N:
        print(*tmp)
        return
    for i in range(1,N+1):
        if i not in tmp:
            tmp.append(i)
            permutation()
            tmp.pop()
permutation()


    
