import sys
si = sys.stdin.readline

n, m = map(int, si().split())
data = list(map(int, si().split()))

array = [0]*11

for x in data:
    array[x] += 1

ans = 0
for i in range(1, m+1):
    n -= array[i]
    ans += array[i]*n

print(ans)