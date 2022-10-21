# 어디에 단어가 들어갈 수 있을까
T = int(input())
def findK(arr, k):
    cnt = 0
    for row in arr:
        for part in ''.join(row).split('0'):
            if len(part)==k:
                cnt+=1
    return cnt

for t in range(1,T+1):
    N, K = map(int,input().split())
    matrix = list()
    transposed_matrix = list([] for _ in range(N))
    for i in range(N):
        row = list(map(str,input().split()))
        matrix.append(row)
        for idx, s in enumerate(row):
            transposed_matrix[idx].append(s)

    ans =0
    ans += findK(matrix,K)
    ans += findK(transposed_matrix,K)

    print(f'#{t} {ans}')