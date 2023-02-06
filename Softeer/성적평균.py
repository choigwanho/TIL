'''
n명의 학생들의 성적이 학번순서대로 주어지고, 학번 구간이 주어졌을 때 이 학생들 성적의 평균을 구하는 문제

학생은 100만, 구간은 1만개, 성적은 100점 만점, 구간은 100만 범위

딱 느낌상 연속적인 값을 구하고 싶고, 학생의 수가 많기 때문에 누적합을 통해서 구하는 것이 합리적으로 보인다.

'''

import sys
si = sys.stdin.readline

n, k = map(int,si().split()) # 학생의 수 n, 구간 수 k
score = [0] + list(map(int, si().split())) # 학생의 성적

for i in range(1,n): # 성적을 누적 처리, 100만
    score[i+1] += score[i]

for _ in range(k): # 구간 정보로 누적 구간 합 O(1)로 계산 및 출력, 1만
    a, b = map(int, si().split()) # 구간 시작, 끝
    print(f"{(score[b]-score[a-1])/(b-a+1):.2f}") # 평균을 구해야 함으로 평균 계산