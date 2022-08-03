# [BOJ_15787 기차가 어둠을 헤치고 은하수를 -Python3](https://www.acmicpc.net/problem/15787)
## 문제분석
'''
```Python
1. 관찰
- 명령에 따라 기차 좌석을 조절해준다.
- 패스한 기차를 기록하여 이후 기차를 보낼지 판단한다.

2. 복잡도
- O(N+M) = 20만 >> 가능

3. 자료구조
- 명령 list[][]
- 패스한 기차 : list[]

```
'''
## 해결코드
import sys
si = sys.stdin.readline

N, M = map(int, si().split())
m_list = list(list(map(int, si().split())) for _ in range(M))

train_list = [[0]*20 for _ in range(N)] # 처음기차에는 아무도 타지 않는다
pass_train = []

for m in m_list:
    m_num, i = m[0], m[1]-1
    t = train_list[i]

    if m_num ==1:
        x = m[2]-1
        if t[x] == 0:
            t[x] = 1
        
    elif m_num ==2:
        x = m[2]-1
        if t[x] == 1:
            t[x] = 0

    elif m_num ==3:
        t[:] = [0]+t[:-1]

    elif m_num ==4:
        t[:] = t[1:]+[0]

ans = 0
for i in range(N):
    if train_list[i] not in pass_train:
        pass_train.append(train_list[i])
        ans+=1

print(ans)