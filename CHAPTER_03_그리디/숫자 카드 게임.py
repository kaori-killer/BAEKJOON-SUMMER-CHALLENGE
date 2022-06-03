def solution(n, m, li):
    answer = 0
    for i in range(n):
        answer = max(answer, min(li[i]))

    return answer


print(solution(2, 4, [[7, 3, 1, 8], [3, 3, 3, 4]]))

