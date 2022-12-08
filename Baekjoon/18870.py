import sys
si = sys.stdin.readline

# n은 100만
n = int(si()) 
# 수직선 위에 N개의 좌표 -> 크기 n의 1차원 배열
l = list(map(int,si().split()))

# index를 통해 순위를 찾기위한 sorted 배열 
sorted_l = sorted(l)

# 좌표 압축을 적용 -> Xi를 압축한 값은 서로 다른 좌표의 개수와 같아야 한다. 

# 좌표 값을 key로 갖는 rank 저장 딕셔너리 사용
rank = dict()
r = 0
for i in sorted_l:
    if i not in rank.keys():
        rank[i] = r
        r+=1

for i in l:
    print(rank[i],end=' ')