'''
# [BOJ_1774 우주신과의 교감 -Python3](https://www.acmicpc.net/problem/1774)

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
def find_parent(n):
    if parent[n] != n:
        parent[n] = find_parent(parent[n])
    return parent[n]

def union_parent(n1,n2):
    n1 = find_parent(n1)
    n2 = find_parent(n2)
    if n1 > n2:
        parent[n1]=n2
    else:
        parent[n2]=n1

from itertools import combinations
import sys
si = sys.stdin.readline

n, m = map(int,si().split()) # o, v

location = [(0,0)]
v_list = []
parent = [node for node in range(n+1)]
for _ in range(n):
    x, y = map(int,si().split())
    location.append((x,y))

for _ in range(m):
    n1,n2 = map(int, si().split())
    if find_parent(n1) != find_parent(n2):
        union_parent(n1,n2)

for n1, n2 in combinations(range(1,n+1),2):
    x1, y1 = location[n1]
    x2, y2 = location[n2]
    dis = ((x2-x1)**2 +(y2-y1)**2)**(1/2)
    v_list.append((dis, n1, n2))

v_list.sort()

ans = 0
for dis, n1, n2 in v_list:
    if find_parent(n1) != find_parent(n2):
        union_parent(n1,n2)
        ans += dis

print(f'{ans:.2f}')