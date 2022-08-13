'''
# [BOJ_2217 로프 -Python3](https://www.acmicpc.net/problem/2217

## 문제분석
```Python
1. 관찰
- n개의 로프
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

n = int(si())
ropes = [int(si()) for _ in range(n)]
ropes.sort(reverse=True)
values = []

for i in range(n):
    values.append(ropes[i]*(i+1)) # 최소값*로프개수 
print(max(values))

