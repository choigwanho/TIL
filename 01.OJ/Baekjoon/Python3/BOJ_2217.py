'''
# [BOJ_2217 로프 -Python3](https://www.acmicpc.net/problem/2217)

## 문제분석
```Python
1. 관찰
- n개의 로프 중 k 개의 로프를 선택하는 모든 경우를 탐색한다.
- K개의 로프중 '가장 w가 작은 로프'에 '로프개수'를 곱한값. 즉, '최소값*로프개수'이 최대 감당 가능한 무게가 된다.

이를 시간 복잡도를 고려해 구현하면
내림차순으로 로프를 정렬하여
'k번째 로프(최소값)*k개의 로프'로 '최대 감당 가능 무게'를 갱신해 값을 구한다.  

2. 복잡도
- O(N) = 1만 가능

3. 자료구조
- 로프 int[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

n = int(si())
ropes = [int(si()) for _ in range(n)]
ropes.sort(reverse=True)
values = []

for i in range(n):
    values.append(ropes[i]*(i+1)) # 최소값*로프개수 
print(max(values))

