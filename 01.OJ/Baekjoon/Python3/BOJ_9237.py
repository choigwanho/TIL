'''
# [BOJ_9237 이장님 초대 -Python3](https://www.acmicpc.net/problem/9237)

## 문제분석
```Python
1. 관찰
- 이장님을 초대할 수 있는 날을 구해라
- 묘목은 하루에 하나씩 심을 수 있고 다 자라는 날은 i+t가 된다
- 오래걸리는 나무순으로 심으면 다 자라고 이장님을 모시면 된다.

2. 복잡도
- O(N) = 100만 >> 가능

3. 자료구조
- 나무, 시간 int[]

```

## 해결코드
```Python
'''
import sys
si = sys.stdin.readline

n = int(si())
trees = list(map(int,si().split()))
trees.sort(reverse=True) # 내림차순 정렬
t_list=[]

for i in range(n):
    t_list.append(i+trees[i])

print(max(t_list)+2)

