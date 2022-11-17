'''
# [BOJ_11650 좌표 정렬하기 -Python3](https://www.acmicpc.net/problem/11650)

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
l = list()

n = int(si())
for _ in range(n):
    x,y = map(int,si().split())
    l.append([x,y])

l.sort(key=lambda x: (x[0],x[1]))

for i in range(n):
    print(l[i][0],l[i][1])