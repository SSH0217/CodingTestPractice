def solution(n):
    answer = 0
    answer = int(''.join(reversed(sorted(str(n)))))
    return answer