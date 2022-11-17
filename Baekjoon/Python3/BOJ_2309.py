'''
# [BOJ_2309 일곱 난쟁이 -Python3](https://www.acmicpc.net/problem/2309)

## 문제분석
```Python
1. 관찰
- 아홉 난쟁이의 키가 중어진다.

!! 잘못 생각 한 풀이 => 난쟁이의 키가 같은 경우를 생각하지 않고 재귀함수로 조합을 구현하려고 했다.
- 9 중 7을 뽑는 모든 경우를 탐색한다. -> 재귀함수로 구현
- 7명의 키 합이 100이 되는 경우 출력한다. -> 7명이 선택된 경우, 합이 100이면 출력

!! 해결 풀이
- 9명중 2을 제거한 모든 경우를 탐색한다.
- 

2. 복잡도
- O(9P2) = (9!)/(2!*8!) >> 가능

3. 자료구조
- 난쟁이 : int[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

dwarves = []
for _ in range(9):
    dwarves.append(int(si()))

dwarves.sort() # 오름차순 정렬

S = sum(dwarves)
sum = 0
for i in range(9):
    for j in range(i+1,9):
        sum = S-dwarves[i]-dwarves[j]
        if sum == 100:
            for d in dwarves:
                if d == dwarves[i]:
                    continue
                if d == dwarves[j]:
                    continue
                else:
                    print(d)
            break
    if sum == 100:
        break
                





