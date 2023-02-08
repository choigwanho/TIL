'''
레일의 순서를 조작할 수 있음

순서변경을 통해 최소한의 무게만 들 수 있음

레일은 n개 이며, 각각 다른 무게를 가짐

레일의 순서가 정해지면 택배 바구니 무게를 넘어가기 전까지 담아 옮겨야 함

순서대로 담야야 하므로 레일의 순서를 건너 뛰어 담을 수 없음

k번 일을 해서 최소한의 무게로 일할 수 있게 레일의 순서를 조정해서 최소값을 만드는 프로그램을 작성

'''

from itertools import permutations
import sys
si = sys.stdin.readline

n, m, k = map(int,si().split()) # 레일의 개수 n, 택배바구니의 무게 m, 일의 시행 횟수 k
w = list(map(int, si().split())) # 택배 레일의 전용 무게

ans = int(1e9)
for case in permutations(w,n): # 레일을 담는 모든 순서 고려
    total = 0
    idx = 0
    for _ in range(k): # k번 일을 함
        tmp = 0 # 한 번 옮기는 무게
        while True: 
            tmp += case[idx%n]
            if tmp > m:# 바구니 한도를 넘으면 현재 이전 물건 적재한 무게까지만 한회 분량으로 더하고 현재 인덱스부터 일 진행
                tmp -= case[idx%n]
                total += tmp
                break   
            idx+=1 
    ans = min(ans, total)
print(ans)