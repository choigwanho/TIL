# 조교의 성적 매기기
T = int(input())
for t in range(1,T+1):
    N, K = map(int,input().split())
    score_arr = list()
    for _ in range(N):
        mid, final, hw = map(int, input().split())
        score = mid*(0.35) + final*(0.45) + hw*(0.2)
        score_arr.append(score)

    k_score = score_arr[K-1]
    score_arr.sort(reverse= True)
    k_rank = score_arr.index(k_score)

    k_grade = k_rank//(N//10)
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

    print(f'#{t} {grade[k_grade]}')