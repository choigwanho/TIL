'''
# [BOJ_3040 백설 공주와 일곱 난쟁이 -Python3](https://www.acmicpc.net/problem/3040)

## 문제분석
```Python
1. 관찰
- 서로 다른 9개중 7개를 만들어야 하므로 2개를 제외하고 합을 구해 100이 되면 출력한다.

2. 복잡도
- O(9C2) = 9!/(2!7!) >> 36 가능

3. 자료구조
- 난쟁이 : int[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

dwarves = list( int(si()) for _ in range(9))
s = sum(dwarves)

for i in range(9):
    for j in range(i+1,9):
        if s-dwarves[i]-dwarves[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else: 
                    print(dwarves[k])
