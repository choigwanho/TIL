from itertools import permutations

def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    n_list = [n for n in numbers]    # O(len(numbers)) = 7
    nums = [] 
    for i in range(1,len(n_list)+1): 
        for num in set(permutations(n_list,i)): # O(len(n_list)Pi) = 7!
            if num[0]=='0':
                continue
            else:
                if isPrime(int(''.join(num))): 
                    answer+=1
    return answer 

testcase = ["17", "011"]
for numbers in testcase:
    print(solution(numbers))