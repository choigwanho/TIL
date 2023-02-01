from collections import Counter
def solution(participant, completion):
    answer = ''
    
    p_counter = Counter(participant)
    for i in completion:
        p_counter[i]-=1

    for k,v in p_counter.items():
        if v>0:
            answer = k
    return answer