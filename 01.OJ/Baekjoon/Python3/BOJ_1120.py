'''
# [BOJ_1120 문자열 -Python3](https://www.acmicpc.net/problem/1120)

## 문제분석
```Python
1. 관찰
- 길이가 다른 두 문자열의 길이를 같게 만들면서 차이를 최소로한다.
- A,B 가 길이가 같도록 만든다

- case1) A, B 길이가 같다.
- case2) A가 들어갈 수 있는 모든 경우를 탐색하여 차이가 가장 적은 경우 출려한다.


2. 복잡도
- O((len(B)-len(A))*len(A)) = 50*50 >> 가능

3. 자료구조
- ans : float -> int
- 두 문자: str[]

```

## 해결코드
```Python
'''
import sys 
si = sys.stdin.readline

a_list, b_list = map(list, si().strip().split()) 
a_len, b_len = len(a_list), len(b_list)
ans=float('inf')

if a_len == b_len:
    tmp = 0
    for i in range(a_len):
        if a_list[i]!=b_list[i]:
            tmp+=1
    ans = tmp
else:
    tmp = 0
    for i in range(b_len-a_len+1):
        for j in range(a_len):
            b_tmp = b_list[i:i+a_len]
            if a_list[j] != b_tmp[j]:
                tmp += 1
        ans = min(tmp, ans)
        tmp=0
print(ans)