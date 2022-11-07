def solution(food):
    temp = ''
    cnt = -1
    for i in food:
        cnt += 1
        if i/2 >= 1 and i != 1:
            for j in range(int(i/2)):
                temp += str(cnt)
    answer = temp + '0' + ''.join(reversed(temp))
    return answer
# def solution(food):
#     answer = ''
#     cnt = 0
#     for f in food:
#         answer += str(cnt) * (f//2)
#         cnt += 1
#     answer = answer + str(0) + answer[::-1]
#     return answer