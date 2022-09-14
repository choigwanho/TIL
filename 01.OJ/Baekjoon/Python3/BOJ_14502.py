'''
# [BOJ_14502 연구소 -Python3](https://www.acmicpc.net/problem/14502)

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
input = sys.stdin.readline

n,m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
q = deque()

def bfs():
    global result

for i in range(n):
    for j in range(m):
        continue