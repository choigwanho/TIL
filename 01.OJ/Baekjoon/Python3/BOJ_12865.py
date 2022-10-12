'''
# [BOJ_12865 평범한 배낭 -Python3](https://www.acmicpc.net/problem/12865)

## 문제분석
```Python
1. 관찰
- N개의 물건이 있다.
- 각 물건은 무게 W와 가치 V를 가진다.
- 최대 K만큼의 무게만을 배낭에 넣을 수 있다.
- 이때, 배낭에 넣을 수 있는 물건들의 가치의 최대값을 알아내야 한다.

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

N, K = map(int, si().split())
stuff = list(list(map(int, si().split())) for _ in range(N))


