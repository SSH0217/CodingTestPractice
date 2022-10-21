# 배열 p y 개수 같으면 true 아니면 false

def solution(s):
    answer = True
    pCnt = 0
    yCnt = 0
    
    for i in s:
        if i == "p" or i == "P":
            pCnt += 1
        elif i == "y" or i == "Y":
            yCnt += 1
    
    if pCnt != yCnt:
        answer = False

    return answer


# return s.lower().count('p') == s.lower().count('y')
# 모두 lower로 바꾸고 개수 세기