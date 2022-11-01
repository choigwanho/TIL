'''
# [BOJ_15565 귀여운 라이언 -Python3](https://www.acmicpc.net/problem/15565)

## 문제분석
```Python
1. 관찰
- N개의 인형이 일렬로 놓여있다.
- 라이언 인형은 1, 어피치 인형은 2
- 라이언 인형이 K개 이상 있는 가장 작은 연속된 인형들의 집합의 크기를 구한다.

- 라이언 인형이 연속된 집합을 찾는다.
- K개 이상 있다?

- 인형의 개수가 1e6(백만) 임으로 선형 복잡도로 해결해야한다.

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

N,K = map(int,si().split()) # 1e6
data = list(map(int,si().split()))




start = 0
end = 0

internal_cnt = 0 
ans = N

for i in range(start,N): # 1e6
    while internal_cnt < K and end < N:
        
        if data[end]==1:
            internal_cnt+=1

        if internal_cnt >= K:
            print(end-start+1)
            ans = min(ans,end-start+1)
        print(start, end, internal_cnt)
        end+=1
print(ans)