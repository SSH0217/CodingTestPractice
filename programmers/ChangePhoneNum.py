# 전화번호 010123123 => *****3123
def solution(phone_number):
    answer = ''
    temp = list(reversed(phone_number))
    for i in range(len(phone_number)):
        if i > 3:
            temp[i] = "*"
    
    answer = ''.join(reversed(temp))
    
    return answer
# return '*' * (len(s) - 4) + s[-4:]