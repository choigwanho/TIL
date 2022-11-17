# [S/W 문제해결 기본] 1일차 - 최빈수 구하기
from collections import Counter
T = int(input())
for t in range(1,T+1):
    num =int(input())
    score = list(map(int, input().split()))
    score_dic = Counter(score)
    max = 0
    ans = 0
    for key, value in score_dic.items():
        if value>max:
            max = value
            ans = key

    print(f'#{num} {ans}')