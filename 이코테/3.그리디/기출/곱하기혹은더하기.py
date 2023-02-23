import sys
si = sys.stdin.readline

data = si()

ans = int(data[0])

for i in range(1, len(data)):
    n = int(data[i])
    if n <= 1 or ans <= 1:
        ans += n
    else:
        ans *= n

print(ans)
