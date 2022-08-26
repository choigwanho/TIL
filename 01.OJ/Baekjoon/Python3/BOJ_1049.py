'''
# [BOJ_1049 기타줄 -Python3](https://www.acmicpc.net/problem/1049)

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

price =[]

N,M = map(int,si().split()) # 끊어진 줄, 브랜드 수
for _ in range(M):
    price.append(list(map(int,si().split())))  # 6줄 패키지, 1줄 가격

s, o, all_s, all_o = N//6, N%6, (N//6)+1,N
m_s, m_o = min(price,key= lambda x:x[0])[0],min(price,key= lambda x:x[1])[1]

print(min((m_s*s + m_o*o),(m_s*all_s),(m_o*all_o)))
