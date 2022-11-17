# 2475 검증수
def sol2475():
    num_list = list(map(int, input().split()))

    for i, v in enumerate(num_list):
        num_list[i]=v**2

    print(sum(num_list)%10)