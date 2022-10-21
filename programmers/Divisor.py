#배열 나누어떨어지는거만 정답에 넣어 정렬
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer


# def solution(arr, divisor):
#     arr = [x for x in arr if x % divisor == 0];
#     arr.sort();
#     return arr if len(arr) != 0 else [-1];