# 1000 A+B
from ast import NotIn
import sys
from operator import index
from tkinter import N

input = sys.stdin.readline

# 1000 A+B
def sol1000():
    a,b = map(int,input().split())
    print(a+b)

# 1001 A-B
def sol1001():
    a,b = map(int,input().split())
    print(a-b)

# 1008 A/B
def sol1001():
    a,b = map(int,input().split())
    print(a/b)

# 1052 단어의 개수
def sol1052():
    word_list = list(map(str,input().split()))
    print(len(word_list))

# 1057 단어 공부
def sol1057():
    char_list = list(str(input()).upper())
    char_set = list(set(char_list))

    cnt_char = [0]*len(char_set)

    max_list = []

    for i, set_char in enumerate(char_set):
        for list_char in char_list:
            if set_char==list_char:
                cnt_char[i]+=1

    for i, cnt in enumerate(cnt_char):
        if max(cnt_char)==cnt:
            max_list.append(char_set[i])

    if len(max_list)==1:
        print(max_list[0])
    else:
        print("?")

# 1330 두 수 비교하기 
def sol1330():
    a,b=map(int,input().split())
    if a<b:
        print("<")
    if a>b:
        print(">")
    if a==b:
        print("==")

# 1546 평균
def sol1546():
    n = int(input())
    score_list= list(map(int, input().split()))

    m = max(score_list)

    for i, v in enumerate(score_list):
        score_list[i]=(v/m)*100

    print(sum(score_list)/n)

# 2438 별 찍기 - 1
def sol2438():
    n = int(input())
    for i in range(1,n+1):
        print("*"*i)

# 2439 별 찍기 - 2
def sol2439():
    n = int(input())
    for i in range(1,n+1):
        print(("*"*i).rjust(n))

# 2475 검증수
def sol2475():
    num_list = list(map(int, input().split()))

    for i, v in enumerate(num_list):
        num_list[i]=v**2

    print(sum(num_list)%10)

# 2557 Hello World
def sol2557():
    print("Hello World!")

# 2562 최대값
def sol2562():
    nums=[]

    for _ in range(9):
        nums.append(int(input()))

    print(max(nums))
    print(nums.index(max(nums))+1)

# 2577 숫자의 개수
def sol2577():
    a = int(input())
    b = int(input())
    c = int(input())

    num_char=list(str(a*b*c))
    num_cnt=0
    for i in range(10):
        for j in num_char:
            if i==int(j):
                num_cnt+=1
        print(num_cnt)
        num_cnt=0

# 2675 문자열 반복
def sol2657():
    n = int(input())
    case=[]
    s=""
    for _ in range(n):
        tmp = list(map(str,input().split()))
        
        for c in tmp[1]:
            s += int(tmp[0])*c
        case.append(s)
        s=""

    for v in case:    
        print(v)

# 2739 구구단
def sol2739():
    n = int(input())

    for i in range(1,10):
        print(f"{n} * {i} = {n*i}")

# 2742 N 찍기
def sol2742():
    for i in range(1,int(input())+1):
        print(i)

# 2742 기찍 N
def sol2742():
    for i in range(int(input()),0,-1):
        print(i)

# 2753 윤년
def sol2753():
    y=int(input())

    if y%4==0:
        if y%100==0:
            if y%400==0:
                print("1")
            else:
                print("0")
        else:
            print("1")
    else:
        print("0")

# 2884 알람 시계
def sol2884():
    h,m=map(int,input().split())

    if m-45<0:
        m = 60+m-45
        if h==0:
            h=23
        else:
            h=h-1
    else:
        m = m-45 
        
    print(h,m)    

# 2908 상수
def sol2908():
    a,b=map(str,input().split())

    if int(a[::-1])>int(b[::-1]):
        print(int(a[::-1]))
    if int(a[::-1])<int(b[::-1]):
        print(int(b[::-1]))

# 2920 음계
def sol2920():
    nums=list(map(int,input().split()))
    cnt=0

    for i in range(7):
        if nums[i]<nums[i+1]:
            cnt+=1

    if cnt==7:
        print("ascending")
    elif cnt==0:
        print("descending")
    else:
        print("mixed")

# 3052 나머지
def sol3052():
    mods=[]

    for _ in range(10):
        mods.append(int(input())%42)

    print(len(list(set(mods))))

# 8958 OX퀴즈
def sol8958():
    add=1
    cnt_list=[]

    for i in range(int(input())):
        cnt_list.append(0)
        tmp = list(str(input()))

        for j in range(len(tmp)):
            if tmp[j]=='O':
                cnt_list[i]=cnt_list[i]+add
                if tmp[j]==tmp[j+1]:
                    add+=1
                else:
                    add=1

    for cnt in cnt_list:
        print(cnt)

# 9498 시험 성적
def sol9498():
    n = int(input())

    if n>=90: print("A")
    elif n>=80: print("B")
    elif n>=70: print("C")
    elif n>=60: print("D")
    else: print("F")

# 10171 고양이
def sol10171():
    print("\    /\\")
    print(" )  ( ')")
    print("(  /  )")
    print(" \(__)|")

# 10172 개
def sol10171():
    print("|\_/|")  
    print("|q p|   /}")
    print('( 0 )"""\\') 
    print('|"^"`    |')
    print('||_/=\\\\__|')

# 10809 알파벳 찾기
def sol10809():
    l1=list(str(input()))
    l2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for i,v in enumerate(l2):
        if v in l1:
            l2[i]=l1.index(v)
        else:
            l2[i]=-1
    for i in l2:
        print(i,end=" ")

# 10818 최소, 최대
def sol10818():
    n = int(input())
    nums=list(map(int,input().split()))

    print(min(nums),max(nums))

# 10869 사칙연산
def sol10869():
    a,b=map(int,input().split())
    print(a+b)
    print(a-b)
    print(a*b)
    print(int(a/b))
    print(a%b)

# 10871 X보다 작은 수
def sol10871():
    n,x=map(int,input().split())
    nums=list(map(int,input().split()))

    for num in nums:
        if num<x:
            print(num,end=" ")

# 10950 A+B - 3
def sol10950():
    sums=[]

    for _ in range(int(input())):
        a,b=map(int,input().split())
        sums.append(a+b)

    for sum in sums:
        print(sum)

# 10951 A+B - 4
def sol10951():
    while True:
        try:
            A, B = map(int, input().split())
            print(A+B)
        except:
            break 

# 10952 A+B - 5
def sol10952():
    a=1
    b=1
    sums=[]
    while a+b!=0:
            a, b = map(int, input().split())
            if a+b!=0:
                sums.append(a+b)

    for sum in sums:
        print(sum)

# 10998	A×B
def sol10998():
    a,b = map(int,input().split())
    print(a*b)

# 11654 아스키 코드
def sol11654():
    print(ord(input()))


# 11720 숫자의 합
def sol11720():
    n=int(input())
    num=list(str(input()))
    sum=0

    for i in num:
        sum+=int(i)

    print(sum)