'''
# [BOJ_1436 영화감독 숌 -Python3](https://www.acmicpc.net/problem/1436)

## 문제분석
```Python
1. 관찰
- 666이 들어간 수를 카운팅
- cnt == N 영화 수 출력 

2. 복잡도
- O(n) 
- N이 10000일때 ans가 266799 임으로 >> 가능

3. 자료구조
- 영화번호, 번째 카운팅: int

```

## 해결코드
```Python
'''
import sys 
si = sys.stdin.readline

N = int(si())

cnt = 0
ans = 666
while True:
    if "666" in str(ans):
        cnt+=1
    if cnt == N: # N번째 제목에 들어간 수 출력후 loop 종료
        print(ans)
        break
    ans+=1