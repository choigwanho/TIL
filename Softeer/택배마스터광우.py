from itertools import permutations
import sys
si = sys.stdin.readline

def move(rail, n, m, k):
    cnt, tmp, carry = -1, 0, 0

    for _ in range(k):
        while tmp <=m:
            cnt = (cnt+1)%n
            tmp += rail[cnt]

        tmp -= rail[cnt]
        cnt -= 1
        carry += tmp
        tmp = 0

    return carry

n, m, k = map(int,si().split()) # 레일의 개수 n, 택배바구니의 무게 m, 일의 시행 횟수 k
w = list(map(int, si().split())) # 택배 레일의 전용 무게

all_move = list()
for rail in permutations(w,n):
    all_move.append(move(rail, n, m, k))
print(*permutations(w,n))
print(min(all_move))