import sys
si = sys.stdin.readline

num = list(map(int,si().split())) # 변속 순서를 나타내는 8개의 숫자

# 변속 순서가 "ascending", "descending", "mixed" 인지 판별 후 출력
dir = 0 # +는 ascending 카운팅, -는 descending 카운팅
for i in range(len(num)-1):
    if num[i+1] > num[i]:
        dir += 1
    elif num[i+1] < num[i]:
        dir -= 1    

if dir == len(num)-1:
    print("ascending")
elif dir == -len(num)+1:
    print("descending")
else:
    print("mixed")