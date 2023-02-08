import sys
si = sys.stdin.readline

t = int(si()) # 테스트 케이스의 개수 t
for num in range(1,t+1):
    a,b = map(int,si().split())
    print(f"Case #{num}: {a+b}")