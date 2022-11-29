'''
# [BOJ_1789 수들의 합 -Python3](https://www.acmicpc.net/problem/1789)

## 문제분석
```Python
1. 관찰
-

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

S = int(si())

ans = 0 
num = 1
while True:
    if num+1>S-num:
        ans+=1
        break
    S-=num
    ans+=1
    num+=1
print(ans)
    
# 다른 풀이
'''
#N까지의 합 : (N+1)*N/2
#(N+1)*N/2 <= S 
S = int(input());
#N(N+1) <= 2S 를 만족하는 N의 최대값
N = int((2*S)**0.5);
while (N*N+N > 2*S):
	N -= 1;
print (N);
'''
    
