'''
# [BOJ_10610 30 -Python3](https://www.acmicpc.net/problem/10610)

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
# 내 풀이
'''
import sys
si = sys.stdin.readline

N = si().strip()

check=[0 for _ in range(len(N))]
num=[]
nums=[]

def make_num():
    if check.count(1)==len(N):
        nums.append(int("".join(num)))
        return
    for i in range(len(N)):
        if not check[i]:
            check[i]=1
            num.append(N[i])
            make_num()
            num.pop()
            check[i]=0

make_num()

nums.sort(reverse=True)

for n in nums:
    if n%30==0:
        print(n)
        break
else:
    print(-1)
'''

import sys
si = sys.stdin.readline

n = list(si().strip())
n.sort(reverse=True)
sum = 0 
if '0' not in n:
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum%3 !=0:
        print(-1)
    else:
        print(''.join(n))
