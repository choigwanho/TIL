'''
# [BOJ_20126 교수님의 기말고사 -Python3](https://www.acmicpc.net/problem/20126)

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

N,M,S = map(int,si().split())
arr =[]
for i in range(N):
    x,y = map(int,si().split())
    arr.append((x,y))
arr.sort()

def sol():
    for i in range(N-1):
        if arr[i+1][0] - (arr[i][0] + arr[i][1]) >= M:
            return arr[i][0] + arr[i][1]

def sol2():
    if arr[-1][0] + arr[-1][1] + M <= S:
        return arr[-1][0] +  arr[-1][1]

if arr[0][0] >= M:
    print(0)
elif sol() != None:
    print(sol())
elif sol2() != None:
    print(sol2())
else:
    print(-1)


