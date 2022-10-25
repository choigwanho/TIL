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

def virus(arr, i, j, visited):
    q = deque([(i,j)])
    visited[i][j]=1
    arr[i][j]=2
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not visited[nx][ny] and arr[nx][ny]!=1:
                visited[nx][ny]=1
                arr[nx][ny]=2
                q.append((nx,ny))

def safeArea(arr, i, j,visited):
    q = deque([(i,j,0)])
    visited[i][j]=1
    rst = 0
    while q:
        x,y,cnt = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not visited[nx][ny] and arr[nx][ny]==0:
                visited[nx][ny]=1
                q.append((nx,ny,cnt+1))
                rst = cnt+1
    for i in range(n):
        print(lab_copy[i])
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


case_list = list(combinations(zero_spot,3))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
for w1,w2,w3 in case_list:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    lab_copy = copy.deepcopy(lab)
    lab_copy[w1[0]][w1[1]] = 1
    lab_copy[w2[0]][w2[1]] = 1
    lab_copy[w3[0]][w3[1]] = 1

    for vx,vy in virus_spot:
        if not visited[vx][vy] and lab_copy[vx][vy] == 2:
            virus(lab_copy,vx,vy,visited)
         
    for zx,zy in zero_spot:
            if not visited[zx][zy] and lab_copy[zx][zy] == 0:
                ans = max(ans,safeArea(lab_copy,zx,zy,visited))
print(ans)