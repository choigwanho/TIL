'''
# [BOJ_1439 뒤집기 -Python3](https://www.acmicpc.net/problem/1439)

## 문제분석
```Python
1. 관찰
- 0 or 1 로 이루어긴 문자열 S
- 모든 숫자를 전부 같게 만들 수 있는 뒤집기의 초소 횟수를 출력

2. 복잡도
- O(N) = 100만 >> 가능

3. 자료구조
- 문자열 str[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

S = list(str(si().strip()))
zero, one = 0, 0
curr =''

for i in range(1,len(S)):
    curr=S[i]
    if S[i-1]!=S[i] and S[i-1]=='0':
        zero += 1
    if S[i-1]!=S[i] and S[i-1]=='1':
        one += 1
 
if curr == '0':
    zero+=1
if curr == '1':
    one+=1

print(min(zero, one))




