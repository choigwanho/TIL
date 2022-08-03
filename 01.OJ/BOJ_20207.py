# [BOJ_20207 달력 -Python3](https://www.acmicpc.net/problem/20207)
## 문제분석
'''
```Python
1. 관찰
- 우선 달력을 만들어준다.
- 일정이 겹치는 경우 행의 수를 +1
- 연속된 일정에서는 일정의 길이 +1로 카운트하며 행의 최대값을 구한다.
- 3의 값으로 직사각형의 크기를 구한다.

- 달력에서 row의 최대값과 col의 길이를 카운트 한 값을 곱해 박스값을 구한다.
!!주의. 끝이 0으로 끝나지 않는 경우가 있다. 이를 마지막에 더해주어야 한다.!!

2. 복잡도
- O(N*(E-S+1)+S) = 365*1000 ... >> 4만정도 가능

3. 자료구조
- 달력 int[]

```
'''
## 해결코드
import sys 
si = sys.stdin.readline

N = int(si())
clndr = [0]*365

for _ in range(N):
    s, e = map(int, si().split())
    for i in range(s-1,e): # 겹치는 일정 높이 +1
        clndr[i] += 1

sum_area = 0
l, h = 0, 0
    
for i in clndr:
    h = max(h,i) 
    if i:
        l += 1
    else:
        sum_area += l*h
        l, h = 0, 0

sum_area += l*h # 끝이 0으로 끝나지 않는 경우

print(sum_area)
    