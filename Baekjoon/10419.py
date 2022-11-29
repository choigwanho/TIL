'''
# [BOJ_10419 지각 -Python3](https://www.acmicpc.net/problem/10419)

## 문제분석
```Python
1. 관찰
- 교수님이 t시간 만큼 지각으로 하시면, s = t**2 만큼 일찍 끝내주신다.
- 수업시간 = t + t**2 인 경우 수업이 바로 끝날 수 있다.


2. 복잡도
- O(t*c) T*C = 100*10000 >> 가능

3. 자료구조
- 테스트케이스, 수업시간 : int

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

T = int(si())
for _ in range(T):
    c = int(si()) # 수업시간
    t = 0
    while True:
        t+=1
        if t+t**2 <= c:
            continue
        else:
            print(t-1)
            break