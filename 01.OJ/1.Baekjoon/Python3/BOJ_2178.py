'''
* 2178 미로 탐색
* https://www.acmicpc.net/problem/2178
1. 아이디어
- 오른쪽 혹은 아래쪽으로 이동하는 것이 최소 거리
2. 복잡도
-
3. 자료구조
-
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
miro = list(input().strip() for _ in range(n))
cnt = 1    # 시작 위치도 칸을 셀 때 포함

xy=[(-1,0),(1,0),(0,-1),(0,1)]     # 상하좌우

x,y=0,0


for i in range(n-1):
    for j in range(m-1):
        if int(miro[i][j+1]): # 우
            cnt+=1
        elif int(miro[i+1][j]): # 하
            cnt+=1
        if x < 0 or x > n or y < 0 or y > m: # 미로를 벗어나는 경우 무시
            pass




if int(miro[x-1][y]): # 상

        pass
    continue
print(cnt)







