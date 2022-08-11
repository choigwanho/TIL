'''
# [BOJ_10162 전자레인지 -Python3](https://www.acmicpc.net/problem/10162)

## 문제분석
```Python
1. 관찰
- 3개의 버튼
- 300초, 60초, 10초
- A,B,B를 눌러 T초가 되도록하는 최소버튼 조작의 경우를 출력한다.

2. 복잡도
- O((T*T*T)//(300*60*10)) = (10000*10000*10000)//(300*60*10) >> 약 천만 가능

3. 자료구조
- 조합: int[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

T = int(si())
flag = float('inf')
ans = [0,0,0]

for i in range(T//300+1):
    for j in range(T//60+1):
        for k in range(T//10+1):
            if 300*i + 60*j +10*k == T:
                flag = min(flag, i+j+k)
                if flag == i+j+k: # 가장 작은 경우 정답리스트 업데이트
                    ans[:]=[i,j,k]

if flag==float('inf'):
    print(-1)
else:
    print(*ans)

