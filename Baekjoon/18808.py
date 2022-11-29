'''
# [BOJ_번호 문제명 -Python3]()

## 문제분석
```Python
[관찰 (전략 설계)]

모눈종이 위에 스티커를 붙인다.
스티커는 상하좌우 연결되어있다.
모눈종이의 크기는 스티커의 크기에 꼭 맞아서 불필요한 행이나 열이 존재하지 않는다.

1. 스티커를 회전시키지 않고 모눈종이를 떼어낸다.

노트북의 범위에 벗어나지 않은 위치 모두 찾기 (loop)

겹치는지 판단하기 (loop)

2-1. 다른 스티커와 겹친 경우
패스

2-2. 다른 스티커와 겹치지 않는 경우
가장 위쪽, 가장 왼쪽의 위치 선정 (반환한 위치를 가장 위쪽, 가장 왼쪽 순으로 loop)
스티커 붙이기

3. 스티커를 붙이지 못한 경우 (conditional)
스티커를 시계 방향으로 90도 회전

4. 한 번 회전하여서 안 된 경우 버린다.


[복잡도 (시간복잡도 검증)]


[자료구조 (자료구조 결정)]


```

## 해결코드
```Python
'''




from itertools import product
import sys
si = sys.stdin.readline

# 노트북의 세로, 가로, 스티커의 개수
N,M,K = tuple(map(int,si().split()))

# K개의 스티커 정보 저장
stickers = []
for i in range(K):
    r,c = map(int,si().split())
    sticker = list(list(map(int,si().split())) for _ in range(r))
    # (r,c,sticker,cnt) 모눈종이의 세로, 가로, 스티커, 회전 횟수
    stickers.append((r,c,sticker,0))

# 스티커를 노트북에 붙여서 채워진 칸의 수
ans = 0 

# 스티커를 시계방향으로 90도씩 회전시킨다.
def rotate90(r,c,s):
    rotated_sticker = []
    for i in range(r):
        for j in range(c):
            print()
    return rotated_sticker

# 스티커를 붙일 수 있는 위치 탐색
def find_pos(s,d):

    return list()
    return []

def simulate(sticker):
    r,c,s,cnt = sticker

    while (cnt<4):

        # 1. 스티커를 회전시키지 않고 모눈종이에서 때어낸다. ( = 방향을 유지한다.)

        # 2-1. 스티커 정보를 넘겨 붙일 수 있는 위치를 찾는다.
        pos = sorted(list(product(range(N-r+1),range(M-c+1))),key= lambda x:(x[0],[1]),reverse=True) if cnt%2==0 else sorted(list(product(range(N-r+1),range(M-c+1))), key= lambda x:(x[0],[1]),reverse=True)

        # 2-2. 붙일 수 있는 곳중에서 가능한 가장 위쪽, 왼쪽의 위치에 붙인다.
        for x,y in pos:
            # 해당 위치에서 스티커가 겹치지 않는지 확인
            
            
        


        # 3. 스티커 회전
        cnt += 1
        s = rotate90(r,c,s)




    print(sticker)

# i번째 스티커를 노트북에 붙이기 
for i in range(K):

    
    simulate(stickers[i])

print()





