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

def cntSafe():
    rst = 0
    for w1,w2,w3 in case_list: # 4만

        lab_copy = copy.deepcopy(lab)
        lab_copy[w1[0]][w1[1]] = 1
        lab_copy[w2[0]][w2[1]] = 1
        lab_copy[w3[0]][w3[1]] = 1

        q = deque(virus_spot) # *64
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if lab_copy[nx][ny]==0: # +64
                    lab_copy[nx][ny]=2
                    q.append((nx,ny))
        
        zero_cnt = 0
        for i in range(n): # +8
            zero_cnt += lab_copy[i].count(0)
        
        rst = max(rst,zero_cnt)
    return rst


from collections import deque
import sys,copy
from itertools import combinations

input = sys.stdin.readline

n,m = map(int, input().split())
zero_spot = []
virus_spot= []
lab = []
for r in range(n):
    row = list(map(int, input().split()))
    lab.append(row) 
    for i, c in enumerate(row):
        if c==0:
            zero_spot.append((r,i))
        elif c==2:
            virus_spot.append((r,i))

case_list = list(combinations(zero_spot,3)) # 0의 좌표 3개의 조합 완전 탐색 (64*63*63)//(3*2) = 약 4만

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(cntSafe())