#배열에서 제일 작은 수 제거하기
def solution(arr):
    answer = []
    temp = arr[0]
    for i in arr:
        if temp > i:
            temp = i
    for i in arr:
        if temp == i:
            arr.pop(arr.index(i))
    answer = arr
    return answer if len(answer) != 0 else [-1]

# return [i for i in mylist if i > min(mylist)]