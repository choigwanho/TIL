# 2941 크로아티아 알파벳

import sys
input = sys.stdin.readline

def sol2941():
    alpabet_list=['c=','c-','dz=','d-','lj','nj','s=','z=']
    word=input().strip()
    cnt=0

    for alpabet in alpabet_list:
        for i in range(len(word)-len(alpabet)+1):
            if alpabet == word[i:i+len(alpabet)]:
                cnt+=1
        word = word.replace(alpabet," ")
    word= word.replace(" ","")

    print(len(word))
    print(cnt+len(word))