'''
# [BOJ_10819 차이를 최대로 -Python3](https://www.acmicpc.net/problem/10819)

## 문제분석
```Python
1. 관찰
- abs(A[0]-A[1]) + abs(A[1] - A[2]) +... + abs(A[N-2]-A[N-1])
- N개의 숫자를 뽑을 수 있는 경우의 수를 모두 고려한다 => N!
- 주어진 수식 for 문으로 구현 => N

- 백트래킹으로 모든 조합 탐색하여 max값 갱신하여 출력

2. 복잡도
- O(N!*N) = 8!*8 >> 가능

3. 자료구조
- 구한 배열: int[]
- 체크처리: int[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

N = int(si())
A = list(map(int, si().split()))

check = [0 for _ in range(N)]
nums = []
ans = 0

def bt():
    global ans
    if len(nums)==N:
        tmp = 0
        for i in range(N-1):
            tmp += abs(nums[i]-nums[i+1])
        ans = max(ans, tmp)
        return
    for i,v in enumerate(A):
        if not check[i]:
            check[i]=1
            nums.append(v)
            bt()
            check[i]=0
            nums.pop()
bt()
print(ans)



