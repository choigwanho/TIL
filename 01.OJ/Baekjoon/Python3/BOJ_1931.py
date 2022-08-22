'''
# [BOJ_1931 회의실 배정 -Python3](https://www.acmicpc.net/problem/1931)

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

n = int(si())
rooms=[]
ans = 1

for _ in range(n):
    start,end = map(int,si().split()) 
    rooms.append((start,end))
rooms.sort(key = lambda x : (x[1],x[0]))

end = rooms[0][1]
for i in range(1,n):
    if rooms[i][0]>=end:
        ans+=1
        end = rooms[i][1]
print(ans)
        
        

