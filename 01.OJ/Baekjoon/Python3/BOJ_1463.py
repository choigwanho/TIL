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

[우선순위]
1. 무조건 3이 좋다 2로 나뉘어져도 3으로 만들어서 나눈다.
2. 


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

while N!=1:
    if N%3!=0: # 3으로 나눠지지 않으면
        N -= 1
        cnt += 1
        if N%2==0:
            N = N//2
            cnt+=1
    else: # 3으로 나눠지면
        N = N//3
        cnt += 1
print(cnt)


    
    


    
