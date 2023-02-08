import sys
si = sys.stdin.readline

n,k = map(int,si().split()) # 라인의 길이 n, 부품을 집을 수 있는 거리 k
line = list(si().strip()) # 로봇과 부품의 위치 -> 로봇 P, 부품 H

ans = 0 # 부품을 집을 수 있는 로봇의 최대 수

for i in range(n):
    if line[i] == "P": # 로봇을 기준으로
        for idx in range(i-k, i+k+1):
            if 0 <= idx < n:
                if line[idx] == "H": # k 범위에 부품이 있으면 가장 왼쪽 부터 선점
                    line[idx] = 0
                    ans += 1
                    break

print(ans)
