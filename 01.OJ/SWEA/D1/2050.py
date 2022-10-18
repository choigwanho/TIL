# 알파벳을 숫자로 변환
ALPHABET = input()
num = ord('A')-1
ans = [ord(s)-num for s in ALPHABET]
print(*ans)