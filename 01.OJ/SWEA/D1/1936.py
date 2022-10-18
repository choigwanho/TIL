# 1대 1 가위바위보
A, B = map(int, input().split())
rsp_dic = {
    1:'가위',
    2:'바위',
    3:'보'
}
if (rsp_dic[A] == '가위' and rsp_dic[B] == '보') or (rsp_dic[A] == '바위' and rsp_dic[B] == '가위') or (rsp_dic[A] == '보' and rsp_dic[B] == '바위'):
    print('A')
elif (rsp_dic[B] == '가위' and rsp_dic[A] == '보') or (rsp_dic[B] == '바위' and rsp_dic[A] == '가위') or (rsp_dic[B] == '보' and rsp_dic[A] == '바위'):
    print('B')

