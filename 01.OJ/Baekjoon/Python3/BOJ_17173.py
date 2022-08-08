'''
# [BOJ_17173 배수들의 합 -Python3](https://www.acmicpc.net/problem/17173)

## 문제분석
```Python
1. 관찰
- 서로다른 M개의 정수 K가 오름차순으로 주어진다.
- 1이상 N 이하인 수의 합을 구해라
=> k의 배수들을 중복없이 모두 찾아 더한다.

2. 복잡도
- O(N*M) = 1000*1000 >> 가능

3. 자료구조
- 배수들 : int[]

```

## 해결코드
```Python
'''
import sys 
si = sys.stdin.readline

N, M = map(int, si().split())
nums = list(map(int, si().split()))
ans = []

for i in range(1,N+1):
    for j in range(M):
        if i%nums[j] == 0 and i not in ans:
            ans.append(i)
print(sum(ans))
