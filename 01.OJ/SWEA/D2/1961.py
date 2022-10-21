# 숫자 배열 회전
def rotate90(arr):
    returnArr = [["" for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            returnArr[i][j] = arr[N-j-1][i]
    return returnArr

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(list(map(str, input().split())) for _ in range(N))

    arr_90 = rotate90(arr)
    arr_180 = rotate90(arr_90)
    arr_270 = rotate90(arr_180)

    print(f'#{t}')
    for i in range(N):
        print("".join(arr_90[i]), "".join(arr_180[i]), "".join(arr_270[i]))