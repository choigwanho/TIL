'''
# [BOJ_16928 뱀과 사다리 게임 -Python3](https://www.acmicpc.net/problem/16928)

## 문제분석
```Python
1. 관찰
- 주사위: 1,2,3,4,5,6
- 내가 원하는 수
- 최소 몇번만에 도착점
- 사다리: 위로 올라감 (번호 커짐)
- 뱀: 아래로 내려감 (번호 작아짐)


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

def bfs():
    q = deque([1])
    while q:
        now = q.popleft()
        if now == 100:
            print(cnt_list[now])
            return 
        for i in range(1,7):
            nxt = now + i
            if nxt<1 or nxt>100:
                continue
            else:
                if nxt in pass_dict:
                    nxt = pass_dict[nxt]
                if not visited[nxt]:        
                    visited[nxt]=1
                    cnt_list[nxt] = cnt_list[now]+1
                    q.append(nxt)

n,m = map(int,si().split()) # 사다리의 수, 뱀의 수
pass_dict = dict() 
for _ in range(n+m):
    x,y = map(int,si().split())
    pass_dict[x]=y
cnt_list = [100]*101
cnt_list[1] = 0
visited = [0]*101

bfs()