'''
# [BOJ_7568 덩치 -Python3](https://www.acmicpc.net/problem/7568)

## 문제분석
```Python
1. 관찰
- 키와 몸무게가 모두 큰 경우 덩치를 크다고 판단한다.
- 조건에 해당 될때 +1을 해준다. 

2. 복잡도
- O(N+N**N+N) = 50 +50**50+50 >> 가능

3. 자료구조
- 신체조건 : list[]
- 몸무게가 큰 사람의 수: dict{int:int}

```

## 해결코드
```Python
'''
from collections import defaultdict
import sys
si = sys.stdin.readline

N = int(si())
p = []
p_dict = defaultdict(int)

for i in range(N):
    p.append(list(map(int,si().split())))
    p_dict[i] =1
for i in range(N):
    for j in range(N):
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            p_dict[i] +=1
for i in p_dict.values():
    print(i, end=" ")