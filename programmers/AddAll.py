# signs 배열 True False따라 양수 음수로 모두 더함
def solution(absolutes, signs):
    answer = 0
    temp = 0
    for i in absolutes:
        if signs[temp] == True:
            answer += i
        else:
            answer -= i
        temp += 1
    
    return answer
# sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))