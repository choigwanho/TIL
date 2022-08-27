'''
# [BOJ_13164 행복 유치원 -Python3](https://www.acmicpc.net/problem/13164)

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

N, K = map(int, si().split())
h = list(map(int,si().split()))
h.sort() # 오름차순 정렬

costs = list() # 차이 값을 모두 계산, 값은 0 ~ N-1 의 인덱스에 매칭된다.
for i in range(N-1):
    costs.append(h[i+1]-h[i])
costs.sort(reverse=True)

print(sum(costs[K-1:])) 
# 오름차순으로 정렬하여 가장 차이가 큰 것들을 경계의 개수(K-1) 만큼 제거하면, 
# 2 2 1 5 -> 2 0 1 0 : 3, 6을 경계로 선택한 것과 같은 결과를 낸다. 


# 시간 초과 (그리디하게 접근해야 풀리는 문제인가보다.)
'''
ans = float('inf')
for i in range(N-1):
    for j in range(i+1,N-1):
        a = h[i]-h[0]
        b = h[j]-h[i+1]
        c = h[-1]-h[j+1]
        ans = min(ans,a+b+c) 
print(ans)
'''
