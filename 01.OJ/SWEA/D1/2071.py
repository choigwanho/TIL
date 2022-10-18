
# 평균값 구하기
T = int(input())
for test_num in range(1, T + 1):
    testcase = list(map(int,input().split()))
    print(f'#{test_num} {round(sum(testcase)/10)}')