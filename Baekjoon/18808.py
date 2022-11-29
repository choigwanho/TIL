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

# 스티커를 시계방향으로 90도씩 회전시킨다.
def rotate90(r,c,s):
    rotated_s = [[0]*r for _ in range(c)] # r,c가 회전함
    for i in range(c):
        for j in range(r):
            rotated_s[i][j] = s[r-j-1][i]
    return (c,r,rotated_s)

# 현재 위치에 스티커를 붙일 수 있는지 확인
def is_attachable(r,c,s,x,y):
    for i in range(r):
        for j in range(c):
            if s[i][j] ==1 and notebook[x+i][y+j]==1:
                return False
    return True

# 현재 위치에 스티커 부착
def attach(r,c,s,x,y):
    for i in range(r):
        for j in range(c):
            if s[i][j]==1:
                notebook[x+i][y+j]=1

def simulate(sticker):
    global N,M
    r,c,s,cnt = sticker

    while cnt<4:

        # 1. 스티커를 회전시키지 않고 모눈종이에서 때어낸다. ( = 방향을 유지한다.)
        # 예외처리 스티거가 회전하여 노트북 범위를 벗어나면 붙일 수 없으므로 회전
        if r > N or c > M:
            r,c,s = rotate90(r,c,s)
            continue

        # 2. 스티커를 붙일 수 있는 위치에서 가능한 가장 위쪽, 왼쪽의 위치에 붙인다.
        is_attached = False
        for i in range(N-r+1):
            for j in range(M-c+1):
                if is_attachable(r,c,s,i,j):
                    attach(r,c,s,i,j)
                    is_attached= True
                    break
            if is_attached:
                break
        if is_attached:
            break
        else:
            # 3. 스티커 회전
            r,c,s = rotate90(r,c,s)
            cnt += 1

import sys
si = sys.stdin.readline

# 노트북의 세로, 가로, 스티커의 개수
N,M,K = map(int,si().split())

# 스티커를 붙일 노트북 배열 초기화
notebook = [[0]*M for _ in range(N)]

# K개의 스티커 정보 저장
stickers = []
for i in range(K):
    r,c = map(int,si().split())
    sticker = list(list(map(int,si().split())) for _ in range(r))
    # (r,c,sticker,cnt) 모눈종이의 세로, 가로, 스티커, 회전 횟수
    stickers.append((r,c,sticker,0))

# i번째 스티커를 노트북에 붙이기 
for i in range(K):
    simulate(stickers[i])

# 스티커를 노트북에 붙여서 채워진 칸의 수 저장
ans = 0 
for i in range(N):
    for j in range(M):
        if notebook[i][j]==1:
            ans+=1

print(ans)