import sys
si = sys.stdin.readline

# 주어진 문자열에서 최대 N개의 종류의 알파벳을 가진 연속된 문자열의 최대 길이

N = int(si()) 
S = si().strip()
cnt = [0]*26
kind = 0

def add(x):
    global kind
    t = ord(x)-ord('a')
    cnt[t] += 1
    if cnt[t] == 1:
        kind += 1

def erase(x):
    global kind
    t = ord(x)-ord('a')
    cnt[t] -= 1
    if cnt[t] ==0:
        kind -= 1

ans=0
L=0
for R in range(len(S)):
    add(S[R])
    while kind > N:
        erase(S[L])
        L += 1
    ans = max(ans,R-L+1)

print(ans)
