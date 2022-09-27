'''
코딩도장
- https://codingdojang.com/scode/408?answer_mode=hide

1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
'''

s= [1, 3, 4, 8, 13, 17, 20]
pair_list = list(zip(s[0:], s[1:]))
pair_list.sort(key=lambda x:x[1]-x[0])
print(pair_list[0])

# 해설 1
m = max(s)
idx = 0 
for i in range(len(s) -1):
    if m > s[i+1]-s[i]:
        idx = i
        m = s[i+1]-s[i]
print(s[i+1], s[i])

# 해설 2
