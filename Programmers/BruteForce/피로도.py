'''
입력과 조건
k: 5000
dungeons: 8*2 = 16
최소 필요 피로도: 던전을 탐험하기 위해 가지고 있어야 하는 피로도
소모 피로도: 던전을 탐험한 후 소모되는 피로도

출력
유저가 탐험할 수 있는 최대 던전 수를 return
'''
from itertools import permutations

def solution(k, dungeons):
  answer = -1 
  l = len(dungeons)
  l_list = [i for i in range(l)]
  for case in list(permutations(l_list, l)): # O(nPr)= 8! => 약 4만
    user = k
    pass_cnt = 0
    for i in case: # *8 => 32만
      if user >= dungeons[i][0]:
        pass_cnt += 1
        user -= dungeons[i][1]
        if answer<pass_cnt:
          answer=pass_cnt
  return answer

testcase = [[80, [[80, 20], [50, 40], [30, 10]]]]
for k, dungeons in testcase:
	print(solution(k, dungeons))