T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))

    ans = 0
    max = n_list[-1]
    for end in range(n-2,-1,-1):
        if max < n_list[end]:
            max = n_list[end]
        else:
            diff = max - n_list[end]
            ans += diff
    print(f'#{test_case} {ans}')