from itertools import product

def solution(users, emoticons):
    answer = []
    
    discount=[10,20,30,40]

    discount_case = list(product(discount, repeat=len(emoticons)))
    
    for case in discount_case:
        register=0
        sale=0
        for u in range(len(users)):
            user_sale = 0
            for e in range(len(emoticons)):
                if case[e]<users[u][0]:
                    continue    
                user_sale += ((100-case[e])//100)*emoticons[e]

            if user_sale >= users[u][1]:
                register+=1
            else:
                sale+=user_sale
                
        answer.append([register, sale])      

    return sorted(answer, key=lambda x:(x[0],x[1])).pop()


testcase= [
    ([[40,10000],[23,10000]], [7000,9000]),
    ([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
]
for users, emoticons in testcase:
    print(solution(users, emoticons))