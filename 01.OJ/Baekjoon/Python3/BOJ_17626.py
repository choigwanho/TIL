'''
# [BOJ_17626 Four Squares -Python3](https://www.acmicpc.net/problem/17626)

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

N = int(si())
rg = 0
tmp = 0
ans = float('inf')
for i in range(int(N**(1/2))+1):
    for j in range(i+1):
        for k in range(j+1):
            for m in range(k+1):
                if i*i + j*j + k*k + m*m == N:
                    if i: tmp+=1
                    if j: tmp+=1
                    if k: tmp+=1
                    if m: tmp+=1
                    ans = min(ans,tmp) 
                    tmp = 0 
print(ans)           

