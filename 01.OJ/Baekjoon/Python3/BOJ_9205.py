'''
# [BOJ_9205 맥주 마시면서 걸어가기 -Python3](https://www.acmicpc.net/problem/9205)

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

# 상근이 집 출발
# 맥주 한박스 20개의 맥주
# 50미터에 한 병씩, 50미터를 가려면 그 직전에 맥주 한 병을 마신다.

from collections import deque
import sys 
si = sys.stdin.readline

def bfs():
    q = deque()
    q.append([home[0],home[1]])
    while q:
        x,y = q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            print("happy")
            return        
        for i in range(n):
            if not visited[i]:
                nx,ny = conv[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx,ny])
                    visited[i] = 1
    print("sad")
    return

t = int(si()) # 테스트 케이스의 개수
for _ in range(t):
    n = int(si()) # 맥주를 파는 편의점의 개수
    home = list(map(int,si().split())) # 상근이네 집
    conv = list(list(map(int,si().split())) for _ in range(n)) # 편의점
    fest =  list(map(int,si().split())) # 송도
    visited = list(0 for _ in range(n+1))
    bfs()



