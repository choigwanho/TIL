'''
LIS (Longest Increasing Subsequence) 최대 부분 증가 수열
'''

def soloution(food):
    arr = list(map(int, food.split()))
    reversed_arr = list(reversed(arr))

    l = len(arr)

    r_lis = [1 for _ in range(l)] # 정방향 LIS

    for i in range(l):
        for j in range(i):
            if arr[i] > arr[j]:
                r_lis[i] = max(r_lis[i], r_lis[j] + 1)

    l_lis = [1 for _ in range(l)] # 역방향 LIS

    for i in range(l):
        for j in range(i):
            if reversed_arr[i] > reversed_arr[j]:
                l_lis[i] = max(l_lis[i], l_lis[j] + 1)

    l_lis.reverse()

    sum_list = list()
    for r, l in zip(r_lis, l_lis):
        sum_list.append(r+l)

    return max(sum_list)-1

    


testcase = ["1 9 8 3 6 3 9 5 1 4 2", 
            "1 2 3 4",
            "98 2 37 5 12",
            "23 32 12 98 3 2 1 9 6 2 12 32 12 3 2 8 45 2 3 21",
            "32 12 98 3 86 42 23 12 2 1 9 6 2 12 32 12 3 2 8 45 2 3 21 37 92 53 68 49 13 87"]

for food in testcase:
    print(soloution(food))
