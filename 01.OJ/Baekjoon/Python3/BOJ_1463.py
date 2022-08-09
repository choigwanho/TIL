'''
# [BOJ_1463 1로 만들기 -Python3](https://www.acmicpc.net/problem/1463)

## 문제분석
```Python
1. 관찰
- 입력: 1000000 => 백만
- N%3 == 0 => nxt = N / 3
- N%2 == 0 => nxt = N / 2
- nxt = N - 1
- 출력: N을 1로 만드는 연산의 최소 횟수 

- 3 으로 나누기, 2로 나누기, 1빼기 순으로 진행할 수로 연산을 줄일 수 있다.

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

N = int(si())
cnt = 0
while True:
    if N == 1:
        break 
    elif N%3==0:
        N = int(N / 3 ) 
        cnt += 1
    elif N%3!=0 and N%2==0:
        N = int(N / 3 )
        cnt += 1
    else:
        N = N - 1
        cnt += 1


    
    


    
