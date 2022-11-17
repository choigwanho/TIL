# 간단한 369게임
N = int(input())
ans = []
for n in range(1, N+1):
    str_n = str(n)
    cnt = 0
    for c in str_n:
        if ('3' == c) or ('6' == c) or ('9' == c):
            cnt+=1
    if cnt:
        ans.append("-"*cnt)
        continue
    ans.append(n)
print(*ans)