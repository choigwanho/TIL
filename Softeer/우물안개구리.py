import sys
si = sys.stdin.readline

def find_loser(a,b): # a,b중 무게가 더 작은 사람을 최고가 아니게 생각하도록하는 함수, 무게가 같아도 최고가 아니다.
    if num[a-1] > num[b-1]:
        best[b-1] = False
    elif num[a-1] < num[b-1]:
        best[a-1] = False
    else: # 무게가 같은 경우 모두 최고가 아님
        best[b-1] = False
        best[a-1] = False
    
n,m = map(int,si().split()) # 회원의 수 n, 회원들 사이의 친분관계 수 m -> 노드와 간선
num = list(map(int,si().split())) # i번 회원이 들 수 있는 역기의 무게

best = list(True for _ in range(n)) # 최고를 디폴트로 초기화

for _ in range(m):
    a,b = map(int,si().split()) # a, b번 회원의 친분 관계
    find_loser(a,b)
    
print(best.count(True))

