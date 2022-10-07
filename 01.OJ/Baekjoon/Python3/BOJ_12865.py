'''
# [BOJ_12865 평범한 배낭 -Python3](https://www.acmicpc.net/problem/12865)

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

while True:
    try:
        N, K  =  map(int, si().split())
        obj_list = []
        for _ in range(N):
            obj_list.append(list(map(int, si().split())))
        
        print(N,K, obj_list)
        

    except ValueError:
        exit(0)