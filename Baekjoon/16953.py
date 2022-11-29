'''
# [BOJ_16953 A → B -Python3](https://www.acmicpc.net/problem/16953)

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
from collections import deque
si = sys.stdin.readline

A,B = map(int,si().strip().split())
ans = 0

q = deque()
q.append((A,1))
while q:
    a, cnt =  q.popleft()
    if a > B: # a가 B보다 큰 경우, q에 추가할 필요가 없다. 자동 종료
        continue
    if a==B:
        print(cnt)
        break
    q.append((a*2,cnt+1))
    q.append((a*10+1,cnt+1)) 
else:
    print(-1)