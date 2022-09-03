'''
# [BOJ_4375 1 -Python3](https://www.acmicpc.net/problem/4375)

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

def sol(num, tmp):
    while True:
        if int(tmp)%num==0:
            print(len(tmp))
            break
        tmp +='1'   

while True:
    try:
        n = int(si())
    except:
        break
    sol(n,'1'*(len(str(n))))
'''

# 참고한 풀이
'''
try - except 예외처리를 해줘야한다.
입력 탈출조건을 제공하지 않기 때문에 EOF(End of File) 예외 처리를 해줘야한다.

규칙을 이용해서 연산을 더 간결하게 해줬다. 
수식으로 쓰고 규칙을 발견하는 연습을 해야겠다.
'''
import sys
si = sys.stdin.readline

while True:
    try:
        n = int(si())
    except:
        break
    num = 0
    ans = 1
    while True:
        num = num*10+1
        num %=n
        if num==0:
            print(ans)
            break
        ans +=1