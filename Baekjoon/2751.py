'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하라

N이 최대 100만이다.

수는 중복되지 않는다.

'''
import sys
si = sys.stdin.readline
print(*sorted(list(int(si()) for _ in range(int(si())))))