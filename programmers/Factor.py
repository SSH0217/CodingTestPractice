def solution(n):
    answer = 0
    for i in range(n):
        if i != 0 and n%i == 0:
            answer += i
    answer += n
    return answer

# return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])