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
doll = list(map(int,si().split()))

ans = -1

start = 0
for i in range(start,N): # 1e6
    cnt = 0
    for j in range(i+1,N):
        if doll[j]==1:
            cnt += 1
        if cnt >= K:
            ans=j-i

print(ans)


