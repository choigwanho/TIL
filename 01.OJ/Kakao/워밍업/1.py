'''
코딩도장
- https://codingdojang.com/scode/393?answer_mode=hide

1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?

8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
(※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)
'''

# 내 풀이
ans = 0
for i in range(1,10001):
     for n in str(i):
        if '8' == n:
            ans+=1
print(ans)

# 해설 풀이 1
# 찾고자 하는 범위를 생각하기 => 전체
# 8이 포함된이 아니라, 전체에 8의 개수 임으로 전체를 스트링으로 변환...!
# 리스트 전체를 String으로 변환하여 8을 세어주면 복잡도 측면에서 가장 좋을 것 같다.
str(list(range(1,10001))).count('8')

# 해설 풀이 2
cnt = 0
for i in range(1,10001):
     for n in str(i):
        if '8' == n:
            cnt+=str(i).count('8')
print(cnt)

# 해설 풀이 3
str(list(i for i in range(1,10001))).count('8')