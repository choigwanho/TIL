"""
# [BOJ_21314 민겸 수](https://www.acmicpc.net/problem/21314)

## 문제 분석
1. 관찰
- 연속된 M은 M의 개수(cnt) -1이 자리수이다 -> 1E(cnt-1)
- K가 있는 경우 -> 5E(cnt)
- K에서 끊어준다.

- M 묶음으로 끊어주면 최소값이 된다.
- M과 K를 묶음으로 해준 경우 최대값이 된다.


2. 복잡도
3. 자료구조

"""

import sys
si = sys.stdin.readline

S = si().strip()
MAX = "" 
MIN = ""
cnt_m = 0  # 연속된 m의 개수 count

for i in range(len(S)):
    if S[i] == 'M':
        cnt_m +=1
    elif S[i] == 'K':
        if cnt_m: # M이 연속된 경우
            MAX += str(5*(10**cnt_m)) # M, K 함께 5의 배수로
            MIN += str(10**cnt_m+5) # M은 1의 배수로, K는 5로 더해서 추가
        else: # K만 단독으로 있는 경우, K는 단독으로 있기 때문에 5로만 끊어서 추가한다.
            MAX += "5"
            MIN += "5"
        cnt_m = 0

if cnt_m: # 끝이 M으로 끝나는 경우
    MIN += str(10**(cnt_m-1))
    while cnt_m: # 최대값을 만들기 위해서는 M의 연속의 경우 1111로 만들어 주어야 함으로 loop
        MAX += "1"
        cnt_m -= 1
    
print(MAX)
print(MIN)
