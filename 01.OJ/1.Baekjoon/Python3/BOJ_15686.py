# [BOJ_15686 치킨 배달 - Python3](https://www.acmicpc.net/problem/15686)
'''
### 문제 접근
```Python
1. 아이디어
- "치킨 거리" = 집과 가장 가까운 치킨집 사이의 거리
- 각각의 집의 치킨거리를 구하여 거리가 먼 치킨집을 배제한다.
-

2. 복잡도
-

3. 자료구조
-
```
'''
### 해결 코드

import sys
si = sys.stdin.readline

N, M = map(int, input().split())
city = [[map(int, input().split())] for _ in range(N)]



