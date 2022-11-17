import sys
from collections import deque
si = sys.stdin.readline

def input():
    N,M = map(int,si().split())

    for r in range(N):
        row = list(map(int,si().split()))
        arr.append(row)
        for c in range(N):
            if row[c]==1: 
                base_arr.append((r,c))

    for _ in range(M):
        x,y = map(int,si().split())
        store_arr.append((x,y))
    
def sol():
    q = deque([])
    for i in range(N):
        print(arr[i])
    print(base_arr)
    print(store_arr)


N,M = 0,0
arr = []
base_arr = []
store_arr = []

if __name__ == "__main__":
    input()
    sol()
