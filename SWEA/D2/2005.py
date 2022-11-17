# 파스칼의 삼각형
T = int(input())
for t in range(1,T+1):
    N = int(input())
    print(f'#{t}')

    pascal = []
    for i in range(N):
        pascal.append([1])
        for j in range(1,i):
            pascal[i].append(pascal[i-1][j-1]+pascal[i-1][j])
        if i!=0:
            pascal[i].append(1)

    for i in range(N):
        print(*pascal[i])