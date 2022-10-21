# Kim 찾아 보내기
def solution(seoul):
    answer = ''
    cnt = 0
    for i in seoul:
        if i == "Kim":
            break;
        cnt += 1
    answer = "김서방은 " + str(cnt) + "에 있다"
    return answer
# "김서방은 {}에 있다".format(seoul.index('Kim'))