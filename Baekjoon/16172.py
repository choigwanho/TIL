# 16172번 나는 친구가 적다 (Large)

import sys, re
si = sys.stdin.readline

s = str(si()) # 알파벳 소문자, 대문자, 숫자로 이루어진 문자열
k = str(si()) # 찾고자 하는 알파벳 소문자, 대문자로만 이루어진 키워드 문자열

m = re.sub('[0-9]+','',s) # 숫자만 찾아서 제거

# 찾고자 하는 키어드가 교과서 내에 존재하면 1, 존재하지 않으면 0 출력
print(1) if k in m else print(0)