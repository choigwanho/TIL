'''
# [BOJ_18352 특정 거리의 도시 찾기 -Python3](https://www.acmicpc.net/problem/18352)

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
si = sys.stdin.readline

N,M,K,X = map(int,si().split()) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
citys = [[] for _ in range(N+1)]


for _ in range(M):
    a,b = map(int,si().split())
    citys[a].append(b)

distance = [-1 for _ in range(N+1)]
distance[X]=0
q = deque([X])
while q:
    i = q.popleft()   
    for nxt in citys[i]:
        if distance[nxt]==-1:
            distance[nxt]=distance[i]+1
            q.append(nxt)   

if K in distance:
    for i,v in enumerate(distance):
        if v==K:
            print(i)
else:
    print(-1)