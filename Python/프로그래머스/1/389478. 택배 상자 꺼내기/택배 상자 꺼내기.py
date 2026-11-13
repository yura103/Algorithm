def solution(n, w, num):  # n: 상자 개수, w: 너비, num: 꺼내려는 상자의 넘버
    answer = 0
    arr = [[] for _ in range(w)]
    for i in range(n):
        j = (i // w)
        if j % 2 == 1:
            k = -(i%w)
            arr[k-1].insert(0, i+1)
        else:
            k = i%w
            arr[k].insert(0, i+1)
    
    for i in range(w):
        answer = 0
        for j in range(len(arr[i])):
            answer += 1
            if arr[i][j] == num:
                return answer