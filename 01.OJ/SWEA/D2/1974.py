# 스도쿠 검증
def getSqaureList(arr, x, y):
    sqaure_list = list()
    for i in range(x, x+3):
        for n in arr[i][y:y+3]:
            sqaure_list.append(n)
    return sqaure_list


T = int(input())
arr_19 = [1,2,3,4,5,6,7,8,9]
for t in range(1,T+1):
    arr = list(list(map(int, input().split())) for _ in range(9))
    cnt = 0
    for i in range(9):
        col = list()
        for j in range(9):
            col.append(arr[j][i])

            if i%3==0 and j%3==0:
                if sorted(getSqaureList(arr,i,j)) != arr_19:
                    cnt+=1
        
        if sorted(arr[i]) != arr_19:
            cnt+=1
        
        if sorted(col) != arr_19:
            cnt+=1   
    
    ans = 0
    if cnt==0:
        ans = 1

    print(f'#{t} {ans}')