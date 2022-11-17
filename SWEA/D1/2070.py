# 큰 놈, 작은 놈, 같은 놈
T = int(input())
for test_num in range(1, T + 1):
    n1,n2 = map(int,input().split())
    ans = ''
    if n1 > n2:
        ans = '>'
    elif n1 < n2:
        ans = '<'
    elif n1 == n2:
        ans = '='
    print(f'#{test_num} {ans}')