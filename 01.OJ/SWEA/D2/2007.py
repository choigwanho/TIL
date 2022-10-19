# 패턴 마디의 길이
T = int(input())
for t in range(1,T+1):
    S = input()
    for i in range(1,11):
        if S == (S[:i]*30)[:30]:
            print(f'#{t} {i}')
            break