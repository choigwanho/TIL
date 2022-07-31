# 1546 평균
def sol1546():
    n = int(input())
    score_list= list(map(int, input().split()))

    m = max(score_list)

    for i, v in enumerate(score_list):
        score_list[i]=(v/m)*100

    print(sum(score_list)/n)