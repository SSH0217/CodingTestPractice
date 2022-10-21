def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    answer /= len(arr)

    # sum(arr)/len(arr) = 평균
    
    return answer