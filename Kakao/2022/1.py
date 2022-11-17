def solution(today, terms, privacies):
    answer = []
    today = 28*12*int(today[2:4]) + 28*int(today[5:7]) + int(today[8:])
    
    term_dic = dict()
    for term in terms:
        t_l = term.split()
        term_dic[t_l[0]] = int(t_l[1])

    num = 0
    for pri in privacies:
        num+=1
        d,t = pri.split()
        d = 28*12*int(d[2:4]) + 28*int(d[5:7]) + int(d[8:])

        if d+28*term_dic[t] <= today:
            answer.append(num)
    
    return answer



testcase= [
    ("2022.05.19",["A 6", "B 12", "C 3"], ["2021.05.02 A","2021.07.01 B","2022.02.19 C","2022.02.20 C"])
]
for today, terms, privacies in testcase:
    print(solution(today, terms, privacies))
