'''
# [BOJ_16234 인구 이동 -Python3](https://www.acmicpc.net/problem/16234)

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
def findMeanAndChange(i,j):
    q = deque([(i,j)])
    visited[i][j] = 1

    cnt = 1
    people = A[i][j]

    record = [(i,j)]
    while q:
        r,c = q.popleft()
        for i in range(4):
            dx, dy = r+dir[i][0], c+dir[i][1]   
            if dx<0 or dx>=N or dy<0 or dy>=N:
                continue
            if visited[dx][dy]:
                continue
        
            if L<= abs(A[r][c]-A[dx][dy])<= R:
                cnt +=1
                people+=A[dx][dy]
                visited[dx][dy] = 1
                q.append((dx,dy))

                record.append((dx,dy))
            
    mean = round(people//cnt)

    for r,c in record:
        A[r][c] = mean

    return cnt


from collections import deque
import sys
si = sys.stdin.readline

N,L,R = map(int,si().split())
A = [list(map(int,si().split())) for _ in range(N)]

dir = [(-1,0),(1,0),(0,-1),(0,1)]

ans =0
while True:
    visited = [[0]*N for _ in range(N)]
    flag = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if findMeanAndChange(r,c)>1:
                    flag = True
    if not flag:
        break
    ans +=1
print(ans)