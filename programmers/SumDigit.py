def solution(n):
    answer = 0
    str(n)
    for i in str(n):
        answer += int(i)
    return answer

# list = [int(i) for i in str(number)]
# return sum(list)