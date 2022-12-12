import sys
si = sys.stdin.readline

def bi(arr, num, lo, hi):
    hi = hi - 1 
    while lo < hi:
        mid = (lo+hi)//2
        if num <= arr[mid]: hi = mid
        else: lo = mid+1
    return lo

# 자연수 N, 1만
n = int(si())
# N개의 정수 A1,A2,...,An
a_arr = list(map(int,si().split()))
# M, 1만
m = int(si())
# M개의 수
x_arr = list(map(int,si().split()))

# M개의 각각의 수들이 A안에 존재하는지 출력
'''
M개의 수를 A에서 그냥 탐색하게 되면 O(n*n) = 1만*1만 -> 1억이다.
a_arr를 주어진 수로 이분탐색하게 되면 O(n*logn) 으로 줄일 수 있다. 
'''
# 이분탐색을 하기위해서 sort
a_arr.sort()

for x in x_arr:
    # 이분탐색으로 idx 탐색
    idx = bi(a_arr, x, 0, n)
    if x == a_arr[idx]:
        print(1)
    else:
        print(0)