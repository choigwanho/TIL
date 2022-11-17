# 몫과 나머지 출력하기
T = int(input())
for test_num in range(1, T + 1):
    n1,n2 = map(int,input().split())
    print(f'#{test_num} {n1//n2} {n1%n2}')