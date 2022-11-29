'''
# [BOJ_14697 방 배정하기 -Python3](https://www.acmicpc.net/problem/14697)

## 문제분석
```Python
1. 관찰
- 가능한지 안한지만 출력하면된다.
- A,B,C는 서로 다른 수 이고, 배수이거나 배수가 아닌 경우로 구분할 수 있다. => 시간복잡도를 줄이기 위해서 분기처리 해보았다.
- 다른 숫자에대해서 나올 수 있는 조합을 구한다. => for문
- DP(top-down, botto-up)풀이. 참조: https://skeo131.tistory.com/91

2. 복잡도
- 서로 다른 경우: O(n*n*n) = 300*300*300 보다 작으므로 가능

3. 자료구조
- int

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

A,B,C,N = map(int, si().split())
flag = False 

if A==1:
    print(1)
else:
    if C%A==0 and B%A==0: # B,C는 A의 배수
        if N%A==0:
            print(1)
        else:
            print(0)
    else:
        if C%B==0: # A,B 조합
            for i in range((N//A)+1):
                for j in range((N//B)+1):
                    if A*i + B*j == N:
                        flag = True
            if flag:
                print(1)
            else:
                print(0)
        else: # A,B,C 조합
            for i in range((N//A)+1):
                for j in range((N//B)+1):
                    for k in range((N//C)+1):
                        if A*i + B*j + C*k == N:
                            flag = True
            if flag:
                print(1)
            else:
                print(0)


