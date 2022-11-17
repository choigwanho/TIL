'''
# [BOJ_10866 덱 -Python3](https://www.acmicpc.net/problem/10866)

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

n = int(si())
tmp = deque()

for _ in range(n):
    order = list(map(str,si().split()))
    od = order[0]
    if od =='push_back':
        tmp.append(order[1])
    if od =='push_front':
        tmp.appendleft(order[1])
    if od =='pop_front':
        if not len(tmp):
            print(-1)
        else:
            print(tmp.popleft())
    if od =='pop_back':
        if not len(tmp):
            print(-1)
        else:
            print(tmp.pop())
    if od =='front':
        if not len(tmp):
            print(-1)
        else:
            print(tmp[0])
    if od =='back':
        if not len(tmp):
            print(-1)
        else:
            print(tmp[-1])
    if od =='size':
        print(len(tmp))
    if od =='empty':
        if not len(tmp):
            print(1)
        else:
            print(0)

    
