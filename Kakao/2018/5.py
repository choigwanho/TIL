import re

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    p = re.compile(r'[a-z]{2}') 

    for i in range(len(str1)-1):
        str1_i = str1[i]+str1[i+1]
        if p.findall(str1_i):
            str1_list.append(str1_i)

    for i in range(len(str2)-1):
        str2_i = str2[i]+str2[i+1]
        if p.findall(str2_i):
            str2_list.append(str2_i)

    inter = set(str1_list) & set(str2_list)
    sum  = set(str1_list) | set(str2_list)

    inter_cnt = 0
    for i in inter:
        str1_list.count(i)
        str2_list.count(i)


    return int((len(inter))/(len(sum))*65536)

testcase = [
    ('FRANCE', 'french'),
    ('handshake', 'shake hands'),
    ('aa1+aa2', 'AAAA12'),
    ('E=M*C^2', 'e=m*c^2')
]

for str1, str2 in testcase:
    print(solution(str1, str2))