import sys
si = sys.stdin.readline

def calMin(s):
    h, m = map(int,s.split(":"))
    return 60*h + m

ans = 0
for i in range(5): # 5일동안 근무
    s, e = map(str,si().split())
    ans += (calMin(e)-calMin(s))
print(ans)