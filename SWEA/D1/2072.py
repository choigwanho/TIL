# 홀수만 더하기
T = int(input())
for test_case in range(1, T + 1):
    tc = list(map(int,input().split()))
    ans = 0
    for n in tc:
        if n%2==0:
            continue
        ans += n
    print(f'#{test_case} {ans}')