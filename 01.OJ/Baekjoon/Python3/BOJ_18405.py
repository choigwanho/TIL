'''
# [BOJ_18405 경쟁적 전염 -Python3](https://www.acmicpc.net/problem/18405)

## 문제분석
```Python
1. 관찰
- 시험관: n*n
- 바이러스: 1~k
- 증식: 상하좌우
- 결과: s초가 지난 후 x,y에 존재하는 바이러스의 종류

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

def bfs(v_dict):
    sorted_v = sorted(v_dict.items(), key=lambda x :x[0])
    new_v = dict()
    for location in sorted_v:
        key = location[0]
        for ty,tx in location[1]:
            for d in [(-1,0),(1,0),(0,-1),(0,1)]:
                ny,nx = ty+d[0],tx+d[1]
                if 0<=ny<n and 0<=nx<n:
                    if test[ny][nx]==0:
                        test[ny][nx]=key
                        if key in new_v:
                            new_v[key].append((ny,nx))
                        else:
                            new_v[key] = [(ny,nx)]

    return new_v
                    
n,k = map(int,si().split())
test=list()
virus = dict()
for i in range(n):
    row = list(map(int,si().split()))
    test.append(row)
    for j in range(n):
        if row[j]:
            if row[j] in virus:
                virus[row[j]].append((i,j))
            else:
                virus[row[j]] = [(i,j)]

s,y,x = map(int,si().split())

for _ in range(s):
    virus = bfs(virus)
    
print(test[y-1][x-1])