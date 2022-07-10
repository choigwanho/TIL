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