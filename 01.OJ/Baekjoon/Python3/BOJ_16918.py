# [BOJ_16918 봄버맨](https://www.acmicpc.net/problem/16918)

## 문제 분석
"""
1. 관찰
- 첫 번째 폭탄이 터진 형태와 두 번째 폭탄이 터진 형태가 3번째 부터 반복된다.
- 첫 폭탄 폭파 3,7,11...
- 둘째 폭탄 폭파 5,9,14...
... 코드 참고

2. 복잡도
- O(R*C) = 200*200*8 >> 가능

3. 자료 구조
- 폭탄 배열: int[][]
"""

## 해결 코드
import sys
si = sys.stdin.readline

R, C, N = map(int, si().split())
board = [list(si().strip()) for _ in range(R)]


if N<=1: # 첫 1초동안은 인풋을 출력
    for li in board: print(''.join(li))
elif N%2 == 0: # 짝수번째는 폭탄이 모두 차 있는 형태
    for i in range(R): print('O'*C)
else: # 첫 폭탄이 터진 이후 3번째 부터 형태가 반복된다. 3,7,11 ... 과 5,9,13...

    bom_1 = [["O"]*C for _ in range(R)] # 첫 폭탄 터짐 
    for i in range(R):
        for j in range(C):
            if board[i][j] == "O":
                for y, x in [(0, 0),(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ny, nx = y+i, x+j
                    if 0 <= ny < R and 0 <= nx < C:
                        bom_1[ny][nx] = '.'
    
    bom_2 = [["O"]*C for _ in range(R)] # 두 번째 폭탄 터짐
    for i in range(R):
        for j in range(C):
            if bom_1[i][j] == "O":
                for y, x in [(0, 0),(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ny, nx = y+i, x+j
                    if 0 <= ny < R and 0 <= nx < C:
                        bom_2[ny][nx] = '.'
                        
    if N%4==3:
        for li in bom_1: print(''.join(li))
    if N%4==1:
        for li in bom_2: print(''.join(li))


