'''
# [BOJ_2164 카드2 -Python3](https://www.acmicpc.net/problem/2164

## 문제분석
```Python
1. 관찰
- queue 에서 두개를 빼서 첫번째 장은 버리고, 두번째 장은 뒤로 보낸다.
- 마지막 한장인 경우 출력한다.

2. 복잡도
- O(n) = 500000 >> 50만 가능

3. 자료구조
- 카드 순서 : int queue

```

## 해결코드
```Python
'''
import sys
from collections import deque
si = sys.stdin.readline

N = int(si())
Q = deque([i for i in range(1,N+1)])

while Q:
    first = Q.popleft()
    if not Q:
        print(first)
        break
    second = Q.append(Q.popleft())
    
