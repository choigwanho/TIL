import sys
si = sys.stdin.readline

n, m = map(int, si().split()) # 구간의 수, 테스트 수
l_and_v = list(list(map(int, si().split())) for _ in range(n)) # 구간의 길이 및 해당 구간에서의 제한 속도
test_l_and_v = list(list(map(int, si().split())) for _ in range(m)) # 테스트하는 구간의 길이와 속도

dp = []
answer = 0
for l, v in l_and_v: # 100*100 = 1만
    for _ in range(l):
        dp.append(v)

idx = 0
for l, v in test_l_and_v: # 100*100 = 1만
    for i in range(l):
        if v - dp[idx] > 0: # 초과한 경우, 최대값으로 갱신
            answer = max(answer, v - dp[idx])
        idx += 1

# 테스트 동안 제한 속도를 가장 크게 벗어난 값 출력, 벗어나지 않은 경우 0을 출력
print(answer)



