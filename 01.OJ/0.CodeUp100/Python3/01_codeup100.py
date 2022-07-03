# 6001 : [기초-출력] 출력하기01(설명)(py)
from asyncio.windows_events import NULL


def sol6001():
    print("Hello")
# 6002 : [기초-출력] 출력하기02(설명)(py)
def sol6002():
    print("Hello World")
# 6003 : [기초-출력] 출력하기03(설명)(py)
def sol6003():
    print("Hello") # print() : 문장 출력 후 줄 바꿈(new line)
    print("World")
# 6004 : [기초-출력] 출력하기04(설명)(py)
def sol6004():
    print("\'Hello\'")
# 6005 : [기초-출력] 출력하기05(설명)(py)
def sol6005():
    print('\"Hello World\"')
# 6006 : [기초-출력] 출력하기06(py)
def sol6006():
    print("\"!@#$%^&*()\'") # \' or \" escape 문을 사용하여 출력
# 6007 : [기초-출력] 출력하기07(py)
def sol6007():
    print("\"C:\\Download\\\'hello\'.py\"") # \도 안전하게 출려하려면 \\를 사용하는 것이 좋다
# 6008 : [기초-출력] 출력하기08(py)
def sol6008():
    print("print(\"Hello\\nWorld\")")
# 6009 : [기초-입출력] 문자 1개 입력받아 그대로 출력하기(설명)(py)
def sol6009():
    c = input()
    print(c)
# 6010 : [기초-입출력] 정수 1개 입력받아 int로 변환하여 출력하기(설명)(py)
def sol6010():
    n = int(input())
    print(n)
# 6011 : [기초-입출력] 실수 1개 입력받아 변환하여 출력하기(설명)(py)
def sol6011():
    f = float(input()) 
    print(f)
# 6012 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기1(설명)(py)
def sol6012():
    a = int(input())
    b = int(input())
    print(a)
    print(b)
# 6013 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기1(py)
def sol6013():
    a = input()
    b = input()
    print(b)
    print(a)
# 6014 : [기초-입출력] 실수 1개 입력받아 3번 출력하기(py)
def sol6014():
    f = float(input())
    print(f)
    print(f)
    print(f)
# 6015 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기2(설명)(py)
def sol6015():
    a, b = map(int, input().split())
    print(a,b, sep='\n') # sep='\n' : 줄바꿈을 두고 출력
# 6016 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기2(설명)(py)
def sol6016():
    c1, c2 = input().split()
    print(c2,c1) # 그냥 , 구분: 줄바꿈을 두고 출력
# 6017 : [기초-입출력] 문장 1개 입력받아 3번 출력하기(설명)(py)
def sol6017():
    s = input()
    print(s, s, s)
# 6018 : [기초-입출력] 시간 입력받아 그대로 출력하기(설명)(py)
def sol6018():
    h, m = input().split(':')
    print(h, m, sep=":")
# 6019 : [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기(py)
def sol6019():
    y, m, d = input().split('.')
    print(d, m, y, sep="-")
# 6020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기(py)
def sol6020():
    a, b = input().split('-')
    print(a, b, sep='')
# 6021 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기(설명)(py)
def sol6021():
    s = input().split()[0]
    print(s[0], s[1], s[2], s[3], s[4], sep='\n')
# 6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기(설명)(py)
def sol6022():
    s = input().split()[0]
    print(s[:2], s[2:4], s[4:])
# 6023 : [기초-입출력] 시분초 입력받아 분만 출력하기(py)
def sol6023():
    s = input().split(":")
    print(s[1])
# 6024 : [기초-입출력] 단어 2개 입력받아 이어 붙이기(설명)(py)
def sol6024():
    w1, w2 = input().split()
    print(w1+w2)
# 6025 : [기초-값변환] 정수 2개 입력받아 합 계산하기(설명)(py)
def sol6025():
    a, b = map(int, input().split())
    print(a+b)
# 6026 : [기초-값변환] 실수 2개 입력받아 합 계산하기(설명)(py)
def sol6026():
    a = float(input()) 
    b = float(input())
    print(a+b)
# 6027 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1(설명)(py)
def sol6027():
    a = int(input()) 
    print("%x" %a) # %x 16진수(hexadecimal) 소문자 형태 문자열로 출력, %o 8진수(octal) 문자열로 출력 
# 6028 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2(설명)(py)
def sol6028():
    a = int(input()) 
    print("%X" %a) # %X 16진수(hexadecimal) 대문자 형태 문자열로 출력
# 6029 : [기초-값변환] 16진 정수 입력받아 8진수로 출력하기(설명)(py)
def sol6029():
    a = int(input(),16) # int(n,16) : int의 두 번째 인자에 원하는 진수, 원하는 진수로 입력
    print("%o" %a) # %o 8진수로 출력
# 6030 : [기초-값변환] 영문자 1개 입력받아 10진수로 변환하기(설명)(py)
def sol6030():
    n = ord(input()) # ord() 입력받은 문자를 10진수 유니코드 값으로 변환 후 저장
    print(n)
# 6031 : [기초-값변환] 정수 입력받아 유니코드 문자로 변환하기(설명)(py)
def sol6031():
    c=int(input())
    print(chr(c)) # chr() 정수 값을 유니코드 문자로 바꿔 출력
# 6032 : [기초-산술연산] 정수 1개 입력받아 부호 바꾸기(설명)(py)
def sol6032():
    n = int(input())
    print(-n) # 단항(unary) 연산자인 -(negative)를 변수 앞에 붙이면 부호가 반대인 값이 된다.
# 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기(설명)(py)
def sol6033():
    c = ord(input()) # ord() 로 입력 받은 문자를 10진수 유니코드 값으로 변환하여 저장, 어떰 문자의 값에 1을 더하면 그 다음 문자의 값이 된다.
    print(chr(c+1)) # chr()  정수값을 문자로 출력
# 6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기(설명)(py)
def sol6034():
    a, b = map(int, input().split())
    print(a-b)
# 6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기(설명)(py)
def sol6035():
    a, b = map(float, input().split())
    print(a*b)
# 6036 : [기초-산술연산] 단어 여러 번 출력하기(설명)(py)
def sol6036():
    w, n = input().split()
    print(w*int(n))
# 6037 : [기초-산술연산] 문장 여러 번 출력하기(설명)(py)
def sol6037():
    n = input()
    s = input() 
    print(int(n)*s) # 문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.
 # 6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기(설명)(py)
def sol6038():
    a, b = map(int, input().split())
    print(a**b) # python 언어에서는 거듭제곱을 계산하는 연산자(**)를 제공한다.일반적으로 수학 식에서 거듭제곱을 표현하는 사용하는 서컴플렉스/케릿 기호(^)는 프로그래밍언어에서 다른 의미로 쓰인다.
# 6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기(py)
def sol6039():
    f1, f2 = map(float, input().split())
    print(f1**f2)
# 6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기(설명)(py)
def sol6040():
    a, b = map(int, input().split())
    print(a//b) # python언어에서는 나눈 몫을 계산하는 연산자(//, floor division)를 제공한다. a//b 와 같이 작성하면, a를 b로 나눈 몫(quotient)을 계산해준다.
# 6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기(설명)(py)
def sol6041():
    a, b = map(int, input().split())
    print(a%b) # python 언어에서는 나눈 나머지를 계산하는 연산자(%, remainder)를 제공한다. a%b 와 같이 작성하면, a를 b로 나눈 나머지(remainder)를 계산해준다.
# 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기(설명)(py)
def sol6042():
    a=float(input())
    print( format(a, ".2f") ) # format(수, ".2f") 를 사용하면 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 준다. 
# 6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
def sol6043():
    f1, f2 = map(float, input().split())
    print( format(f1/f2,".3f") ) # python 언어에는 나눗셈(division)을 계산하는 연산자(/)가 있다.
# 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)
def sol6044():
    a, b = map(int, input().split())
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
    print(format(a/b,'.2f'))
# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)
def sol6045():
    a, b, c = map(int, input().split())
    sum = a+b+c
    mean= format(sum/3,'.2f')
    print(sum, mean)
# 6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기(설명)(py)
def sol6046():
    n = int(input()) 
    print(n<<1)
    """
    *2 를 계산한 값을 출력해도 되지만,
    정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용할 수 있다.
    컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,
    2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
    지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

    왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
    오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
    가장 오른쪽에 있는 1비트는 사라진다.

    n = 10
    print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
    print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
    print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
    print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

    정수 10의 2진수 표현은 ... 1010 이다.
    10 << 1 을 계산하면 ... 10100 이 된다 이 값은 10진수로 20이다.
    10 >> 1 을 계산하면 ... 101 이 된다. 이 값은 10진수로 5이다.
    """ 
    """
    n = 10 에서 10 은 10진수 정수 값으로 인식된다.
    변수 n 에 문자열을 저장하고 싶다면, n = "10" 또는 n = '10'으로 작성해 넣으면 되고,
    n = 10.0 으로 작성해 넣으면 자동으로 실수 값으로 저장된다.
    n = 0o10 으로 작성해 넣으면 8진수(octal) 10으로 인식되어 10진수 8값이 저장되고,
    n = 0xf 나 n = 0XF 으로 작성해 넣으면 16진수(hexadecimal) F로 인식되어 10진수 15값으로 저장된다.
    """
# 6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)
def sol6047():
    a, b = map(int, input().split())
    print(a<<b)
# 6048 : [기초-비교연산] 정수 2개 입력받아 비교하기1(설명)(py)
def sol6048():
    a, b = map(int, input().split())
    if(a<b): print('True') # 비교/관계연산자, <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.
    else: print('False')
# 6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2(설명)(py)
def sol6049():
    a, b = map(int, input().split())
    if(a==b): print('True') # 수학에서 왼쪽과 오른쪽의 계산 결과가 같음(동치)을 나타내는 기호 =(equal sign) 1개는 프로그래밍언어에서는 전혀 다른 의미로 사용된다.
    else: print('False')
# 6050 : [기초-비교연산] 정수 2개 입력받아 비교하기3(설명)(py)
def sol6050():
    a, b = map(int, input().split())
    if(b>=a): print('True')
    else: print('False')
# 6051 : [기초-비교연산] 정수 2개 입력받아 비교하기4(설명)(py)
def sol6051():
    a, b = map(int, input().split())
    if(a!=b): print('True')
    else: print('False')
# 6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기(설명)(py)
def sol6052():
    n = int(input()) # 입력된 값이 0이면 False, 0이 아니면 True 를 출력한다.
    print(bool(n)) # bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력해준다.
# 6053 : [기초-논리연산] 참 거짓 바꾸기(설명)(py)
def sol6053():
    a = bool(int(input()))
    print(not a) # 어떤 불 값이나 변수에 not True, not False, not a 와 같은 계산이 가능하다. 참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서 not 예약어(reserved word, keyword)를 사용할 수 있다.
# 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)
def sol6054():
    a, b = map(int, input().split())
    print(bool(int(a)) and bool(int(b))) # 둘 다 True 일 경우에만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)
def sol6055():
    a, b = map(int, input().split())
    print(bool(int(a)) or bool(int(b))) # 하나라도 참일 경우 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
# 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)
def sol6056():
    a, b = map(int, input().split())
    c = bool(a)
    d = bool(b)
    print((c and (not d)) or ((not c) and d)) # 두 값의 True / False 값이 서로 다를 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)
def sol6057():
    a, b = map(int, input().split())
    c = bool(a)
    d = bool(b)
    print(((not c) and (not d)) or (c and d)) # 두 값의 True / False 값이 서로 같을 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
#
def sol6058():
    a, b = map(int, input().split())
    c = bool(a)
    d = bool(b)
    print(((not c) and (not d)))
# 6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기(설명)(py)
def sol6059():
    n=int(input())
    print(~n)
    """
    입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
    비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)      
    
    ** 비트단위(bitwise) 연산자는,
    ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
    <<(bitwise left shift), >>(bitwise right shift)
    가 있다.

    예를 들어 1이 입력되었을 때 저장되는 1을 32비트 2진수로 표현하면
         00000000 00000000 00000000 00000001 이고,   
    ~1은 11111111 11111111 11111111 11111110 가 되는데 이는 -2를 의미한다.

    예시
    a = 1
    print(~a) #-2가 출력된다.

    참고
    컴퓨터에 저장되는 모든 데이터들은 2진수 형태로 바뀌어 저장된다.
    0과 1로만 구성되는 비트단위들로 변환되어 저장되는데,
    양의 정수는 2진수 형태로 바뀌어 저장되고, 음의 정수는 "2의 보수 표현"방법으로 저장된다.

    양의 정수 5를 32비트로 저장하면, 

    5의 2진수 형태인 101이 32비트로 만들어져
    00000000 00000000 00000000 00000101
    로 저장된다.(공백은 보기 편하도록 임의로 분리)

    32비트 형의 정수 0은
    00000000 00000000 00000000 00000000

    그리고 -1은 0에서 1을 더 빼고 32비트만 표시하는 형태로
    11111111 11111111 11111111 11111111 로 저장된다.

    -2는 -1에서 1을 더 빼면 된다.
    11111111 11111111 11111111 11111110 로 저장된다.

    이러한 내용을 간단히 표현하면, 정수 n이라고 할 때,

    ~n = -n - 1
    -n = ~n + 1 과 같은 관계로 표현할 수 있다.
    """
# 6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기(설명)(py)
def sol6060():
    a,b=map(int,input().split())
    print(a&b)
# 6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기(설명)(py)
def sol6061():
    a,b=map(int,input().split())
    print(a|b)
# 6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기(설명)(py)
def sol6062():
    a,b=map(int,input().split())
    print(a^b)
# 6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)
def sol6063():
    a,b=map(int,input().split())
    print(int(a if (a>=b) else b))
# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)
def sol6064():
    a,b,c=map(int,input().split())
    print(int((a if a<b else b) if ((a if a<b else b)<c) else c))
# 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)(py)
def sol6065():
    a,b,c=list(map(int,input().split()))
    if a%2 == 0: print(a)
    if b%2 == 0: print(b)
    if c%2 == 0: print(c)
# 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)
def sol6066():
    a,b,c=list(map(int,input().split()))
    if a%2 == 0: print("even")
    else: print("odd")
    if b%2 == 0: print("even")
    else: print("odd")
    if c%2 == 0: print("even")
    else: print("odd")
# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)
def sol6067():
    n = int(input())
    if n<0:
        if n%2==0: print('A')
        else: print('B')
    else:
        if n%2==0: print('C')
        else: print('D')
# 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)
def sol6068():
    score = int(input())
    if (score>=90): print('A')
    elif(90>score>=70): print('B')
    elif(79>score>=40): print('C')
    else: print('D')
# 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)
def sol6069():
    a = input()
    if a=='A': print("best!!!")
    elif a=='B': print("good!!")
    elif a=='C': print('run!')
    elif a=='D': print("slowly~")
    else: print("what?")
# 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)
def sol6070():
    m = int(input())
    if (m//3==0) or (m//3==4): print("winter")
    if (m//3==1): print("spring")
    if (m//3==2): print("summer")
    if (m//3==3): print("fall")
# 6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기(설명)(py)
def sol6071():
    n = 1
    while n!=0:
        n = int(input())
        if n!=0: print(n)
# 6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)(py)
def sol6072():
    n = int(input())
    while n!=0:
        print(n)
        n=n-1
# 6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(py)
def sol6073():
    n = int(input())
    while n>0:
        print(n-1)
        n=n-1
# 6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)
def sol6074():
    c = ord(input()) # ord(), 문자를 정수값으로
    t = ord('a') 
    while t<=c :
        print(chr(t), end=' ') # chr(), 정수값을 문자로
        t += 1
# 6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)
def sol6075():
    n = int(input())
    a = 0
    while a<=n:
        print(a)
        a=a+1
# 6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2(설명)(py)
def sol6076():
    n = int(input())
    for i in range(n+1) :
        print(i)    
# 6077 : [기초-종합] 짝수 합 구하기(설명)(py)
def sol6077():
    n = int(input())
    s = 0
    for i in range(1, n+1) :
        if i%2==0 :
            s += i
    print(int(s))
# 6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(py)
def sol6078():
    c = ''
    while c!="q":
        c=input()
        print(c)
# 6079 : [기초-종합] 언제까지 더해야 할까?(py)
def sol6079():
    n = int(input())
    s=0
    for i in range(1,n):
        s=s+i
        if s>=n: 
            print(i)
            break
# 6080 : [기초-종합] 주사위 2개 던지기(설명)(py)
def sol6080():
    n,m=map(int,input().split())
    for i in range(1, n+1) :
      for j in range(1, m+1) :
        print(i, j)
# 6081 : [기초-종합] 16진수 구구단 출력하기(py)
def sol6081():
    n = int(input(),16) # 16진수로 입력 받기
    for i in range(1,16):
        print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
# 6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)
def sol6082():
    n = int(input())
    for i in range(1, n+1) :
        if i//10==3 : print("X", end=' ')
        elif i%10==3 : print("X", end=' ')
        elif i%10==6 : print("X", end=' ')
        elif i%10==9 : print("X", end=' ')
        else: print(i)
# 6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
def sol6083():
    r,g,b=map(int,input().split())
    cnt=0
    for i in range(r):
        for j in range(g):
            for k in range(b):
                print(i,j,k)
                cnt=cnt+1
    print(cnt)
# 6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)
def sol6084():
    h, b, c, s = map(int, input().split())
    print(format((h*b*c*s)/8/1024/1024,".1f"),"MB")
# 6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)
def sol6085():
    w, h, b = map(int, input().split())
    print(format((w*h*b)/8/1024/1024,".2f"),"MB")
# 6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)
def sol6086():
    n = int(input())
    s = 0
    c = 1
    while True :
        s += c
        c += 1
        if s>=n :
            break   
    print(s)
# 6087 : [기초-종합] 3의 배수는 통과(설명)(py)
def sol6087():
    n = int(input())
    for i in range(1, n+1) :
        if i%3==0 :
            continue            
        print(i, end=' ')
# 6088 : [기초-종합] 수 나열하기1(py)
def sol6088():
    a,d,n = map(int,input().split())
    print(a+d*(n-1))  
# 6089 : [기초-종합] 수 나열하기2(py)
def sol6089():
    a,r,n = map(int,input().split())
    print(a*(r**(n-1)))
# 6090 : [기초-종합] 수 나열하기3(py)
def sol6090():
    a,m,d,n = map(int,input().split())
    for _ in range(1,n):
        a = a*m+d
    print(a)
# 6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)
def sol6091():
    a,b,c=map(int,input().split())
    d = 1
    while d%a!=0 or d%b!=0 or d%c!=0 :
        d += 1
    print(d)
# 6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)
def sol6092():
    n = int(input())
    a = list(map(int,input().split()))
    d = list()

    for i in range(24):
        d.append(0)

    for i in range(n):
        d[a[i]]+=1
         
    for i in range(1,24):
        print(d[i], end=' ')
# 6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)
def sol6093():
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n-1, -1, -1) :
        print(a[i], end=' ')
# 6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)
def sol6094():
    int(input())
    a = list(map(int,input().split()))
    print(min(a)) 
# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)
def sol6095():
    d=[]
    for i in range(20):
        d.append([])
        for j in range(20):
            d[i].append(0)
    
    n = int(input())
    for i in range(n):
        x,y=input().split()
        d[int(x)][int(y)]=1

    for i in range(1,20):
        for j in range(1,20):
            print(d[i][j], end=' ')
        print()
# 6096 [기초-리스트] 바둑알 십자 뒤집기(py)
def sol6096():
    d = [ list(map(int, input().split())) for _ in range(19) ]

    for i in range(int(input())):
        x,y=map(int,input().split())
        for j in range(19):
            if d[j][y-1]==0:
                d[j][y-1]=1
            else:
                d[j][y-1]=0

            if d[x-1][j]==0:
                d[x-1][j]=1
            else :
                d[x-1][j]=0

    for i in range(19):
        for j in range(19):
            print(d[i][j],end=" ")
        print()

# 6097 [기초-리스트] 설탕과자 뽑기(py)
def sol6097():
    h,w = map(int, input().split())
    sticks=list(list(map(int,input().split())) for _ in range(int(input())))

    game=[[0]*w for _ in range(h)]

    for stick in sticks:
        l = stick[0]
        d = stick[1]
        x = stick[2]
        y = stick[3]
        for i in range(l):
            if d==0:
                for a in range(y-1,y+l-1):
                    game[x-1][a]=1
            if d==1:
                for a in range(x-1,x+l-1):
                    game[a][y-1]=1

    for i in range(h):
        for j in range(w):
            print(game[i][j],end=" ")
        print()

# 6098 [기초-리스트] 성실한 개미(py)
def sol6098():
    miro = list(list(map(int,input().split())) for _ in range(10))

    x=1
    y=1

    for i in range(y,10):


        if miro[i][x]==1:
            break
        if miro[i][x]==2:
            miro[i][x]=9
            break

        for j in range(x,10):
            if miro [i][j]==0:
                miro[i][j]=9
                x=j
            if miro[i][j]==1:
                break
            if miro[i][j]==2:
                miro[i][j]=9
                break
            
    for i in range(10):
        for j in range(10):
            print(miro[i][j],end=" ")
        print()