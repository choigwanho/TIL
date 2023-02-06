'''
1초 간격으로 바이러스 침입
바이러스는 1초당 p배씩 증가
n초 동안 죽는 바이러스는 없음
매초 침입하는 바이러스의 숫자가 주어질 때, n초 후에 총 몇 마리의 바이러스를 잡아야 하는지 출력
'''
import sys
si = sys.stdin.readline

p, n = map(int, si().split()) # 증가율 p, 총 시간 n(초)
virus = list(map(int, si().split())) # 매초 침입하는 바이러스의 숫자 a
 
ans = 1
for v in virus:
    ans = v%int(1e9+7)

print()